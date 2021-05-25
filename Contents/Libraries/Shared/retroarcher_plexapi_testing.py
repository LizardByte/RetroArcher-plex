#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import sys
import argparse
from plexapi.server import PlexServer, CONFIG
import xmltodict, json

#************import when needed for faster execution?
#import uuid

PLEX_URL = ''
PLEX_TOKEN = ''

agent = 'org.github.agent.retroarcher.retroarcher.xml'

# ## CODE BELOW ##
if not PLEX_URL:
    PLEX_URL = CONFIG.data['auth'].get('server_baseurl')
if not PLEX_TOKEN:
    PLEX_TOKEN = CONFIG.data['auth'].get('server_token')

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
account = plex.myPlexAccount()
'''
#examples
#sections = plex.library.sections()
#print(sections)
#sections_dict = {x.key: x.title for x in sections}
#print(sections_dict)
settings = plex.settings.all()
#<Setting:ConfigurationUrl:http://127.0.0.1:324>
#print(settings)
#url = plex.settings.ConfigurationUrl
#print(url)

def pluginDir():
    if sys.platform == 'win32':
        #appdata = plex.settings.get('LocalAppDataPath') #this would be much faster... but devs say it only works on windows???
        #appdata = str(appdata).replace('<Setting:LocalAppDataPath:', '').replace('>', '')
        appdata = plex.settings.LocalAppDataPath
        #print(appdata)
        pluginDir = os.path.join(appdata, 'Plex Media Server', 'Plug-ins')
        
    else:
        import uuid
        logDir = str(uuid.uuid4())

        logs = plex.downloadLogs(savepath=logDir, unpack=True) #https://discord.com/channels/183396325142822912/283629564087762945/795820408766988308
        #print(logs)

        os.rename(os.path.join(logDir, 'Plex Media Server.log'), os.path.join(logDir, 'Plex Media Server.0.log'))

        x = 0
        y = 0
        for root, dir, files in os.walk(logDir): #https://stackoverflow.com/a/35703223
            for f in files:

                i = os.path.join(logDir, f)

                if f.startswith('Plex Media Server.'):
                    if x < 6 and y < 2:
                        #print(f)
                        
                        inputFile = open (i, 'rb')
                        data = inputFile.readlines()
                        inputFile.close()
                        
                        #for line in data: #https://thispointer.com/5-different-ways-to-read-a-file-line-by-line-in-python/
                        for line in data: #https://thispointer.com/5-different-ways-to-read-a-file-line-by-line-in-python/
                            if 'Scanning for plug-ins in' in line.decode('UTF-8'):
                                pluginDir = os.path.abspath(line.decode('UTF-8').split('"')[-2])
                                y += 1
                        x += 1
                os.remove(i)
        os.rmdir(logDir)

    #print(pluginDir)
    return(pluginDir)

def pluginSettings(directory):
    settingsFile = os.path.join(os.path.dirname(directory), 'Plug-in Support', 'Preferences', agent )
    return settingsFile

pluginDir = pluginDir()
print(pluginDir)
pluginSettings = pluginSettings(pluginDir)
print(pluginSettings)

inputFile = open (pluginSettings, 'rb')
j = xmltodict.parse(inputFile)
print(json.dumps(j, indent=4))

SourceRomDir = os.path.abspath(j['PluginPreferences']['sSourceRomDirectory'])
SourceRomFolderStyle = int(j['PluginPreferences']['sSoureRomFolderStyle'])

print(SourceRomDir)
print(SourceRomFolderStyle)
'''


'''
item = plex.fetchItem(109974)
item.uploadTheme(url='https://gamethemesongs.com/song/download/12052')
themes = item.themes()
print(themes)

item = plex.fetchItem(105259)
#item.uploadTheme(url='https://gamethemesongs.com/song/download/12052')
themes = item.themes()
print(themes)
'''

item = plex.fetchItem(105258)
item.uploadTheme(url='https://gamethemesongs.com/song/download/12052')
themes = item.themes()
print(themes)

#all = plex.library.all()
#print(all)
'''
sections = plex.library.sections()
sections_dict = {x.key: x.title for x in sections}

print(sections_dict)

libraries = []

for key, value in sections_dict.items():
    if value.lower().startswith('retroarcher') or value.lower().endswith('retroarcher'):
        libraries.append(value)

print(libraries)

for x in libraries:
    movies = plex.library.section(x).all()
    for y in movies:
        print(y)
        print(y.locations)
        print(y.ratingKey)
    
#print(movies)
'''
