# -*- coding: utf-8 -*-
# plex debugging
import sys
if 'plexscripthost' not in sys.executable.lower():
    from plexagents.builtins import Prefs, Log

import requests
import urllib3
from plexapi.server import PlexServer


def setup_plexapi():
    plex_url = Prefs['url_PlexServer']
    plex_token = Prefs['str_PlexToken']

    Log.Info('Plex url: ' + str(plex_url))
    
    if not plex_token:
        Log.Info('Plex token not set in agent settings, cannot proceed')
        return False
    Log.Info('Plex token is set in settings!')

    sess = requests.Session()
    # Ignore verifying the SSL certificate
    sess.verify = False  # '/path/to/certfile'
    # If verify is set to a path to a directory,
    # the directory must have been processed using the c_rehash utility supplied
    # with OpenSSL.
    if sess.verify is False:
        # Disable the warning that the request is insecure, we know that...
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # create the plex server object
    plex = PlexServer(plex_url, plex_token, session=sess)

    return plex


def add_themes(theme_list, rating_key):
    plex = setup_plexapi()
    
    if plex:
        for theme_file in theme_list:
            Log.Info(theme_file)
            plex_item = plex.fetchItem(int(rating_key))
            plex_item.uploadTheme(filepath=theme_file)  # to upload from url use 'url=theme_url' instead
