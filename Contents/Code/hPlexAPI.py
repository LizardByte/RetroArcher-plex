# -*- coding: utf-8 -*-
import requests
from plexapi.server import PlexServer

def setup_plexapi():
    PLEX_URL = Prefs['PLEX_URL']
    PLEX_TOKEN = Prefs['PLEX_TOKEN']

    Log.Info('Plex url: ' + str(PLEX_URL))
    
    if PLEX_TOKEN == None:
        Log.Info('Plex token not set in agent settings, cannot proceed')
        return False
    Log.Info('Plex token is set in settins!')

    sess = requests.Session()
    # Ignore verifying the SSL certificate
    sess.verify = False  # '/path/to/certfile'
    # If verify is set to a path to a directory,
    # the directory must have been processed using the c_rehash utility supplied
    # with OpenSSL.
    if sess.verify is False:
        # Disable the warning that the request is insecure, we know that...
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #create the plexapi server
    plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)
    #account = plex.myPlexAccount()

    return plex

def add_themes(theme_list, rating_key):
    plex = setup_plexapi()
    
    if plex != False:
        for x in theme_list:
            Log.Info(x)
            plex_item = plex.fetchItem(int(rating_key))
            plex_item.uploadTheme(filepath=x)
            #plex_item.uploadTheme(url=x)

