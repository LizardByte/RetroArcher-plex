# -*- coding: utf-8 -*-
import os
import json

import hPlexAPI

#url = 'https://raw.githubusercontent.com/ReenigneArcher/RetroArcher.database/main/themeSongs.json'

load_file = Core.storage.load

audio_extensions = ['.mp3', '.m4a']

def Themes(self, metadata, media, lang, force, movie, game):
    game_name = game[2]
    game_version = game[3]
    game_platform = game[4]
    short_name = game_name.split('(', 1)[0].strip()
    
    #themeDB = JSON.ObjectFromURL(url, values=None, headers={}, cacheTime=1, encoding=None, errors=None, timeout=60, sleep=0)
    #Log.Info(themeDB)
    #Log.Info(type(themeDB))
    
    theme_songs = []
    
    #old json method... not doing this now
    '''
    for id in themeDB:
        try:
            if game_name in themeDB[id]['gamePlatforms'][game_platform]:
                theme_songs.append(themeDB[id]['url'])
        except KeyError:
            pass
    
    Log.Info(theme_songs)
    '''
    
    #delete existing theme songs
    Log.Info(metadata.themes)
    themes_length = len(metadata.themes)
    x = 0
    while x < themes_length:
        Log.Info(metadata.themes[x])
        del metadata.themes[x]
        x += 1
    Log.Info(metadata.themes)
    
    themeDir = Prefs['dir_SourceThemeDirectory']
    found = False

    if themeDir != None:
        for x in audio_extensions:
            if found == False:
                path = [os.path.join(themeDir, game_platform, game_name + x), os.path.join(themeDir, game_platform, short_name + x)]
                Log.Info(path)
                for y in path:
                    if os.path.exists(y):
                        theme_songs.append(y)
                        Log.Info('found theme song!')
                        found = True
                        break

        '''
        y = 0
        for x in theme_songs:
            Log.Info(x)
            
            theme_data = load_file(x)
            #theme_data = HTTP.Request(x) #for a url instead
            
            metadata.themes[game_name] = Proxy.Media(theme_data, sort_order = y)
            metadata.themes.validate_keys(game_name)
            y += 1
        '''
        for x in metadata.themes:
            Log.Info(x)
        
        hPlexAPI.add_themes(theme_songs, media.id)

