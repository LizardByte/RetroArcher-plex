from functools import partial
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import argparse
import logging
import multiprocessing as mp
import re
import requests
import time
import xml.etree.ElementTree as ET

# Library version
__version__ = "1.8.1"


# String used to prefix local sitemaps
LOCAL_PREFIX = "file://"


def format_archive_url(url):
    """Given a URL, constructs an Archive URL to submit the archive request."""
    logging.debug("Creating archive URL for %s", url)
    SAVE_URL = "https://web.archive.org/save/"
    request_url = SAVE_URL + url

    return request_url


def call_archiver(request_url, rate_limit_wait, session):
    """Submit a url to the Internet Archive to archive."""
    if rate_limit_wait > 0:
        logging.debug("Sleeping for %s", rate_limit_wait)
        time.sleep(rate_limit_wait)
    logging.info("Calling archive url %s", request_url)
    r = session.head(request_url, allow_redirects=True)
    try:
        # Raise `requests.exceptions.HTTPError` if 4XX or 5XX status
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.exception(e)
        raise


def get_namespace(element):
    """Extract the namespace using a regular expression."""
    match = re.match(r"\{.*\}", element.tag)
    return match.group(0) if match else ""


def download_remote_sitemap(sitemap_url, session):
    """Download the sitemap of the target website."""
    logging.debug("Downloading: %s", sitemap_url)
    r = session.get(sitemap_url)
    try:
        # Raise `requests.exceptions.HTTPError` if 4XX or 5XX status
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.exception(e)
        raise
    else:
        return r.text.encode("utf-8")


def load_local_sitemap(sitemap_filepath):
    """Load a local sitemap and return it as a string."""
    logging.debug("Loading local sitemap: %s", sitemap_filepath)

    if sitemap_filepath.startswith(LOCAL_PREFIX):
        sitemap_filepath = sitemap_filepath[len(LOCAL_PREFIX):]

    # Try to open the file, error on failure
    try:
        logging.debug("Opening local file '%s'", sitemap_filepath)
        with open(sitemap_filepath, "r") as fp:
            contents = fp.read()
    except IOError as e:
        logging.exception(e)
        raise

    return contents


def sitemap_is_local(sitemap_url):
    """Returns True if we believe a URI to be local, False otherwise."""
    return sitemap_url.startswith(LOCAL_PREFIX) or sitemap_url.startswith("/")


def extract_pages_from_sitemap(site_map_text):
    """Extract the various pages from the sitemap text. """
    root = ET.fromstring(site_map_text)

    # Sitemaps use a namespace in the XML, which we need to read
    namespace = get_namespace(root)

    urls = []
    for loc_node in root.findall(".//{}loc".format(namespace)):
        urls.append(loc_node.text)

    return set(urls)


def main():
    # Command line parsing
    parser = argparse.ArgumentParser(
        prog="archiver",
        description="A script to backup a web pages with Internet Archive",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    parser.add_argument(
        "urls",
        nargs="*",
        default=[],
        help="the URLs of the pages to archive",
    )
    parser.add_argument(
        "--file",
        help="path to a file containing urls to save (one url per line)",
        required=False,
    )
    parser.add_argument(
        "--sitemaps",
        nargs="+",
        default=[],
        help="one or more URIs to sitemaps listing pages to archive; local paths must be prefixed with '{f}'".format(f=LOCAL_PREFIX),
        required=False,
    )
    parser.add_argument(
        "--log",
        help="set the logging level, defaults to WARNING",
        dest="log_level",
        default=logging.WARNING,
        choices=[
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ],
    )
    parser.add_argument(
        "--log-to-file",
        help="redirect logs to a file",
        dest="log_file",
        default=None,
    )
    parser.add_argument(
        "--archive-sitemap-also",
        help="also submit the URL of the sitemap to be archived",
        dest="archive_sitemap",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--jobs",
        "-j",
        help="run this many concurrent URL submissions, defaults to 1",
        default=1,
        type=int,
    )
    parser.add_argument(
        "--rate-limit-wait",
        help="number of seconds to wait between page requests to avoid flooding the archive site, defaults to 5; also used as the backoff factor for retries",
        dest="rate_limit_in_sec",
        default=5,
        type=int,
    )

    args = parser.parse_args()

    # Set the logging level based on the arguments
    #
    # If `filename` is None, the constructor will set up a stream, otherwise it
    # will use the file specified.
    logging.basicConfig(level=args.log_level, filename=args.log_file)

    logging.debug("Arguments: %s", args)

    archive_urls = []
    # Add the regular pages
    if args.urls:
        logging.info("Adding page URLs to archive")
        logging.debug("Page URLs to archive: %s", args.urls)
        archive_urls += map(format_archive_url, args.urls)

    # Set up retry and backoff
    session = requests.Session()

    retries = Retry(
        total=5,
        backoff_factor=args.rate_limit_in_sec,
        status_forcelist=[500, 502, 503, 504],
    )

    session.mount("https://", HTTPAdapter(max_retries=retries))
    session.mount("http://", HTTPAdapter(max_retries=retries))

    # Download and process the sitemaps
    remote_sitemaps = set()
    logging.info("Parsing sitemaps")
    for sitemap_url in args.sitemaps:

        # Save the remote ones, incase the user wants us to backthem up
        if sitemap_is_local(sitemap_url):
            logging.debug("The sitemap '%s' is local.", sitemap_url)
            sitemap_xml = load_local_sitemap(sitemap_url)
        else:
            logging.debug("The sitemap '%s' is remote.", sitemap_url)
            if args.archive_sitemap:
                remote_sitemaps.add(sitemap_url)
            sitemap_xml = download_remote_sitemap(sitemap_url, session=session)

        for url in extract_pages_from_sitemap(sitemap_xml):
            archive_urls.append(format_archive_url(url))

    # Archive the sitemap as well, if requested
    if args.archive_sitemap:
        logging.info("Archiving sitemaps")
        if remote_sitemaps:
            archive_urls += map(format_archive_url, remote_sitemaps)
        else:
            logging.debug("No remote sitemaps to backup.")

    # And URLs from file
    if args.file:
        logging.info("Reading urls from file: %s", args.file)
        with open(args.file) as file:
            urls_from_file = (u.strip() for u in file.readlines() if u.strip())
        archive_urls += map(format_archive_url, urls_from_file)

    # Deduplicate URLs
    archive_urls = set(archive_urls)

    # Archive the URLs
    logging.debug("Archive URLs: %s", archive_urls)
    pool = mp.Pool(processes=args.jobs)
    partial_call = partial(
        call_archiver, rate_limit_wait=args.rate_limit_in_sec, session=session
    )
    pool.map(partial_call, archive_urls)
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
