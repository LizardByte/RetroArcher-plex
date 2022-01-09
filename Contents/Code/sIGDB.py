# -*- coding: utf-8 -*-
import datetime
import json

# imports from Libraries\Shared
import requests
from igdb.wrapper import IGDBWrapper

# plex globals
from plex_builtins import *

# local imports
import common


class Extras:
    type_order = ['trailer', 'teaser', 'gameplay', 'interview']

    type_map = {
        'trailer': TrailerObject,
        'teaser': TrailerObject,
        'gameplay': OtherObject,
        'interview': InterviewObject
    }

    '''
    #known object types
    #https://github.com/contrary-cat/LocalTVExtras.bundle/blob/284985343edf2b64e475602210804410fba4fadc/Contents/Code/__init__.py
    #https://github.com/piplongrun/TrailerAddict.bundle/blob/master/Contents/Code/__init__.py
    BehindTheScenesObject
    DeletedSceneObject
    FeaturetteObject
    InterviewObject
    OtherObject
    SceneOrSampleObject
    ShortObject
    TrailerObject

    #possible object types
    ExtraObject
    '''


def igdb_wrapper():
    url = Prefs['url_IgdbCreds']
    
    authorization = JSON.ObjectFromURL(url, values=None, headers={}, cacheTime=86400, encoding=None, errors=None, timeout=60, sleep=0)
    
    wrapper = IGDBWrapper(authorization['client_id'], authorization['access_token'])

    return wrapper


def get_youtube(id, api_key):
    base_url = 'https://www.googleapis.com/youtube/v3/videos?id='
    url = base_url + id
    url = base_url + id +'&key=' + api_key + '&part=snippet' #https://developers.google.com/youtube/v3/getting-started
    
    headers = {
            'Accept': 'application/json'
        }
    
    result = load_json(url, headers)
    return result


def load_json(url, headers):
    result = requests.get(url=url, headers=headers).json()
    return result


def post_json(url, headers):
    result = requests.post(url=url, data=headers).json()
    return result


def year(timestamp):
    timestamp = datetime.datetime.fromtimestamp(timestamp)
    #year = timestamp.strftime('%Y')
    year = timestamp.year
    return year

#not being used (using archer_dict)
age_rating_category = {
    1 : 'ESRB',
    2 : 'PEGI'
    }

age_rating_rating = {
    1 : ['Three', 3],
    2 : ['Seven', 7],
    3 : ['Twelve', 12],
    4 : ['Sixteen', 16],
    5 : ['Eighteen', 18],
    6 : ['RP', 13],
    7 : ['EC', 3],
    8 : ['E', 6],
    9 : ['E10', 10],
    10 : ['T', 13],
    11 : ['M', 17],
    12 : ['AO', 18]
    }

multiplayer_mode = {
    'campaigncoop' : 'Multiplayer Mode: Campaign Co-op',
    'dropin' : 'Multiplayer Mode: Drop in',
    'lancoop' : 'Multiplayer Mode: LAN Co-op',
    'offlinecoop' : 'Multiplayer Mode: Offline Co-op',
    'offlinecoopmax' : 'Multiplayer Mode: Offline Co-op Max: ',
    'offlinemax' : 'Multiplayer Mode: Offline Max: ',
    'onlinecoop' : 'Multiplayer Mode: Online Co-op',
    'onlinecoopmax' : 'Multiplayer Mode: Online Co-op Max: ',
    'onlinemax' : 'Multiplayer Mode: Online Max: ',
    'splitscreen' : 'Multiplayer Mode: Splitscreen',
    'splitscreenonline' : 'Multiplayer Mode: Online Splitsceen'
}

igdb_enums = {
    'age_rating_category' : {
        1 : 'ESRB',
        2 : 'PEGI'
    },
    'age_rating_rating' : {
        1 : {
            'rating' : 'Three',
            'age': 3
            },
        2 : {
            'rating' : 'Seven',
            'age': 7
            },    
        3 : {
            'rating' : 'Twelve',
            'age': 12
            },
        4 : {
            'rating' : 'Sixteen',
            'age': 16
            },
        5 : {
            'rating' : 'Eighteen',
            'age': 18
            },
        6 : {
            'rating' : 'RP',
            'age': 13
            },
        7 : {
            'rating' : 'EC',
            'age': 3
            },
        8 : {
            'rating' : 'E',
            'age': 6
            },
        9 : {
            'rating' : 'E10',
            'age': 10
            },
        10 : {
            'rating' : 'T',
            'age': 13
            },
        11 : {
            'rating' : 'M',
            'age': 17
            },
        12 : {
            'rating' : 'AO',
            'age': 18
            }
    },
    'character' : {
        'gender' : {
            0 : 'Male',
            1 : 'Female',
            2 : 'Other'
        },
        'species' : {
            1 : 'Human',
            2 : 'Alien',
            3 : 'Animal',
            4 : 'Android',
            5 : 'Unknown'
        }
    },
    'platform_type' : {
        1 : 'console',
        2 : 'arcade',
        3 : 'platform',
        4 : 'operating_system',
        5 : 'portable_console',
        6 : 'computer'
    }
}


def Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform, site_index):
    gamePlatform = game_platform
    gameName = str(game_name)
        
    gameNameList = [gameName]
    Log.Info(gameNameList)
    
    #last_length = 0
    last_list0 = []
    last_list1 = gameNameList
    
    #while len(gameNameList) != last_length:
    while last_list0 != last_list1:
        last_list0 = sorted(list(set(gameNameList)))
        Log.Info(len(gameNameList))
        Log.Info('last_list0 :' + str(last_list0))
        Log.Info(type(last_list0))
        for x in gameNameList:
            gameNameList.append(x.replace('-', ':'))
            gameNameList.append(x.replace('-', ' '))
            gameNameList.append(x.replace('&', ' and '))
            gameNameList.append(x.replace('!', ' '))
            gameNameList.append(x.split('-', 1)[0].strip())
            gameNameList.append(x.split('-', 1)[-1].strip())
            gameNameList.append(x.rsplit(' ', 1)[0].strip())
            gameNameList = sorted(list(set(gameNameList))) #remove duplicates
        #gameNameList = sorted(list(set(gameNameList))) #remove duplicates
        
        #Log.Info(len(gameNameList))
            
        #last_length = len(gameNameList)
        last_list1 = sorted(list(set(gameNameList)))
        Log.Info(type(last_list1))
        Log.Info('last_list1 :' + str(last_list1))
        
        if last_list0 == last_list1:
            break
        else:
            Log.Info('not equal')
            Log.Info('last_list0 :' + str(last_list0))
            Log.Info('last_list1 :' + str(last_list1))
    
    x = 0
    for value in gameNameList:
        gameNameList[x] = common.double_space_replace(value)
        x += 1

    Log.Info(gameNameList)
    
    wrapper = igdb_wrapper()
    #Log.Info(wrapper)
    
    #search
    end_point = 'games'
    fields = 'first_release_date, name, alternative_names.name, platforms, release_dates.y, release_dates.platform'
    limit = 500

    for gameNameSearch in gameNameList:
        byte_array = wrapper.api_request(
            end_point,
            'search "' + gameNameSearch + '"; fields ' + fields + '; where release_dates.platform = (' + str(gamePlatform) + '); limit ' + str(limit) + ';'
        )
        jsonSearch = json.loads(byte_array)
        Log.Info(json.dumps(jsonSearch, indent=2))
        
        result_id_list = []
        
        x = 0
        for key in jsonSearch:
            result_id = str(jsonSearch[x]['id'])
            
            if result_id not in result_id_list: #only add this title if it's not already in the results list
                result_id_list.append(result_id)
                
                '''release dates'''
                jsonKey = 'release_dates'
                
                try:
                    result = jsonSearch[x][jsonKey]
                    Log.Info(json.dumps(result, indent=2))
                    y = 0
                    date = ''
                    for key in result:
                        if result[y]['platform'] == gamePlatform: #if release date platform == gamePlatform
                            result_year = result[y]['y']
                            break
                        
                        y += 1
                    if date == '':
                        try:
                            result_year = year(jsonSearch[x]['first_release_date'])
                        except KeyError:
                            pass
                    
                except KeyError:
                    pass
                
                
                result_name = jsonSearch[x]['name']
                
                #compare the title to the search string
                a, b = gameName, result_name
                result_score = 100 - 100*Util.LevenshteinDistance(a, b) / max(len(a),len(b)) if a!=b else 100
                
                '''alternative names'''
                jsonKey = 'alternative_names'
                
                try:
                    result = jsonSearch[x][jsonKey]
                    Log.Info(json.dumps(result, indent=2))
                    y = 0
                    for key in result:
                        temp_name = result[y]['name']
                        Log.Info('temp_name: ' + str(temp_name))
                        #compare the title to the search string
                        a, b = gameName, temp_name
                        temp_score = 100 - 100*Util.LevenshteinDistance(a, b) / max(len(a),len(b)) if a!=b else 100
                        Log.Info('temp_score: ' + str(temp_score))
                        
                        if temp_score > result_score:
                            result_score = temp_score
                            result_name = temp_name
                        
                        y += 1
                    
                except KeyError:
                    pass

                #jsonSearch[x]['lang'] = lang # site doesn't list language, just use Plex language
                result_lang = lang
                
                results.Append( MetadataSearchResult(
                    id = '{' + gameName + '}{' + game_version + '}{' + str(gamePlatform) + '}{' + archer_dict.dSiteShortNames1[site_index] + '-' + result_id + '}', #need many variables to build this in the update function
                    #id = archer_dict.dSiteShortNames1[site_index] + '-' + result_id, #can't do this or all versions with igdb id get combined to a single entry
                    name = result_name,
                    year = result_year,
                    lang = result_lang,
                    score = result_score
                ) )
            
            x += 1
    
    #search alternative names
    end_point = 'alternative_names'
    fields = 'name, game.first_release_date, game.name, game.alternative_names.name, game.platforms, game.release_dates.y, game.release_dates.platform'
    #fields = 'name, game.name'
    limit = 500

    for gameNameSearch in gameNameList:
        byte_array = wrapper.api_request(
            end_point,
            'fields ' + fields + '; where name ~ *"' + gameNameSearch + '"* & game.release_dates.platform = (' + str(gamePlatform) + '); limit ' + str(limit) + ';'
        )
        jsonSearch = json.loads(byte_array)
        Log.Info(json.dumps(jsonSearch, indent=2))
        
        result_id_list = []
        
        x = 0
        for key in jsonSearch:
            try:
                result_id = str(jsonSearch[x]['game']['id'])
                
                if result_id not in result_id_list: #only add this title if it's not already in the results list
                    result_id_list.append(result_id)
                    
                    '''release dates'''
                    jsonKey = 'release_dates'
                    
                    try:
                        result = jsonSearch[x]['game'][jsonKey]
                        Log.Info(json.dumps(result, indent=2))
                        y = 0
                        date = ''
                        for key in result:
                            if result[y]['platform'] == gamePlatform: #if release date platform == gamePlatform
                                result_year = result[y]['y']
                                break
                            
                            y += 1
                        if date == '':
                            try:
                                result_year = year(jsonSearch[x]['first_release_date'])
                            except KeyError:
                                result_year = None
                        
                    except KeyError:
                        pass
                    
                    
                    result_name = jsonSearch[x]['name']
                    
                    #compare the title to the search string
                    a, b = gameName, result_name
                    result_score = 100 - 100*Util.LevenshteinDistance(a, b) / max(len(a),len(b)) if a!=b else 100
                    
                    '''alternative names'''
                    jsonKey = 'alternative_names'
                    
                    try:
                        result = jsonSearch[x]['game'][jsonKey]
                        Log.Info(json.dumps(result, indent=2))
                        y = 0
                        for key in result:
                            temp_name = result[y]['name']
                            Log.Info('temp_name: ' + str(temp_name))
                            #compare the title to the search string
                            a, b = gameName, temp_name
                            temp_score = 100 - 100*Util.LevenshteinDistance(a, b) / max(len(a),len(b)) if a!=b else 100
                            Log.Info('temp_score: ' + str(temp_score))
                            
                            if temp_score > result_score:
                                result_score = temp_score
                                result_name = temp_name
                            
                            y += 1
                        
                    except KeyError:
                        pass

                    #jsonSearch[x]['lang'] = lang # site doesn't list language, just use Plex language
                    result_lang = lang
                    
                    results.Append( MetadataSearchResult(
                        id = '{' + gameName + '}{' + game_version + '}{' + str(gamePlatform) + '}{' + archer_dict.dSiteShortNames1[site_index] + '-' + result_id + '}', #need many variables to build this in the update function
                        name = result_name,
                        year = result_year,
                        lang = result_lang,
                        score = result_score
                    ) )
            except KeyError:
                pass
                
            x += 1
    
    Log.Info(results)
    
    results.Sort('score', descending=True)


def Update(self, metadata, media, lang, force, movie, game):
    Log.Info(game)
    #site_index = game[0]
    id = game[1]
    game_name = game[2]
    Log.Info(game_name)
    gameVersion = game[3]
    platformName = game[4]
    
    wrapper = igdb_wrapper()
    
    end_point = 'games'
    fields = 'age_ratings.category, age_ratings.rating, aggregated_rating, artworks.url, collection.name, cover.url, franchises.name, game_modes.name, genres.name, involved_companies.company.name, involved_companies.developer, multiplayer_modes.*, name, player_perspectives.name, rating, release_dates.date, release_dates.y, release_dates.platform, screenshots.url, summary, storyline, themes.name, videos.name, videos.video_id'
    limit = 1

    byte_array = wrapper.api_request(
        end_point,
        'fields ' + fields + '; where id = ' + str(id) + '; limit ' + str(limit) + ';'
    )
    jsonGame = json.loads(byte_array)
    Log.Info(json.dumps(jsonGame, indent=2))

    '''summary'''
    summary = ''
    try:
        summary += jsonGame[0]['summary']
    except KeyError:
        Log.Info('summary not found')
    
    try:
        summary += '\n\nStoryline: ' + jsonGame[0]['storyline']
    except KeyError:
        Log.Info('storyline not found')
    
    if summary != '':
        metadata.summary = summary
    
    '''title'''
    title = "%s [%s] %s" % (jsonGame[0]['name'], platformName, gameVersion)
    metadata.title = title.strip()
    
    '''platform id'''
    for key, value in archer_dict.dPlatformMapping.items():
        #Log.Info(key)
        if platformName == key:
            gamePlatform = str(archer_dict.dPlatformMapping[key]['systemIds']['igdb'])
            break
    
    '''critic rating'''
    try:
        #metadata.rating = jsonGame[0]['total_rating'] / 10 #combined rating
        metadata.rating = jsonGame[0]['aggregated_rating'] / 10 #critic rating
        if metadata.rating >= 5.0:
            rating_image = 'rating_up.png'
        else:
            rating_image = 'rating_down.png'
        metadata.rating_image = '/:/plugins/com.github.agents.retroarcher.retroarcher/resources/%s' % rating_image
    except KeyError:
        Log.Info('critic rating not found')
    
    '''audience rating'''
    try:
        metadata.audience_rating = jsonGame[0]['rating'] / 10 #audience rating
        if metadata.audience_rating >= 5.0:
            rating_image = 'rating_up.png'
        else:
            rating_image = 'rating_down.png'
        metadata.audience_rating_image = '/:/plugins/com.github.agents.retroarcher.retroarcher/resources/%s' % rating_image
    except KeyError:
        Log.Info('audience rating not found')
    
    '''studio'''
    jsonKey = 'involved_companies'
    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            if result[x]['developer'] == True:
                try:
                    studio = result[x]['company']['name']
                    metadata.studio = studio
                    break
                        
                except KeyError:
                    Log.Info('developer not found')
                
            x += 1
    except KeyError:
        pass

    
    '''release dates'''
    #add a way to get relase date based on version (region) of rom
    jsonKey = 'release_dates'
    
    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        date = ''
        for key in result:
            if result[x]['platform'] == gamePlatform:
                metadata.year = result[x]['y']
                date = result[x]['date']
                metadata.originally_available_at = datetime.datetime.fromtimestamp(date)
                
                break
            
            x += 1
        if date == '':
            try:
                metadata.originally_available_at = datetime.datetime.fromtimestamp(jsonGame[0]['first_release_date'])
            except KeyError:
                Log.Info('first release date not found')
        
    except KeyError:
        Log.Info('platform release date not found')
    
    '''content_rating/content_rating_age'''
    #age_ratings --> content rating
    preferred_rating_system = archer_dict.dict_enum_agent_map['PreferredRatingSystem'][Prefs['enum_PreferredRatingSystem']]['igdb'] #need to get preference value in same format as value from json
    Log.Info(preferred_rating_system)

    jsonKey = 'age_ratings'
    
    try:
        result = jsonGame[0][jsonKey]
        Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            Log.Info(key)
            content_rating = igdb_enums['age_rating_rating'][result[x]['rating']]['rating']
            content_rating_age = igdb_enums['age_rating_rating'][result[x]['rating']]['age']
            if result[x]['category'] == preferred_rating_system:
                break
            
            x += 1
        metadata.content_rating = content_rating
        metadata.content_rating_age = content_rating_age
    except KeyError:
        Log.Info('content rating not found')

    '''posters'''
    
    #cover --> poster
    jsonKey = 'cover'

    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        
        x = 0
        image = 'https:' + result['url'].replace('/t_thumb/', '/t_original/')
        image_name = 'igdb-' + game_name
        
        metadata.posters[image_name] = Proxy.Media(HTTP.Request(image), sort_order = x)
        Log.Info("sTHEGAMESDB.Update() - Posters['%s']: '%s'" % (image_name, image))
        
    except KeyError:
        Log.Info('poster not found')

    '''art'''
    y = 0
    #artworks --> fanart
    jsonKey = 'artworks'
    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            image = 'https:' + result[x]['url'].replace('/t_thumb/', '/t_original/')
            
            if image not in metadata.art:
                metadata.art[image] = Proxy.Media(HTTP.Request(image), sort_order = y)
                Log.Info("sTHEGAMESDB.Update() - Fanarts['%s']: '%s'" % (x, image))
                y += 1
            else:
                Log.Info("sTHEGAMESDB.Update() - Fanarts['%s'] already in database: '%s'" % (x, image))
            
            x += 1
        
    except KeyError:
        Log.Info('artworks not found')


    #screenshots --> fanart
    jsonKey = 'screenshots'
    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        
        x = 0
        for key in result:
            image = 'https:' + result[x]['url'].replace('/t_thumb/', '/t_original/')
            
            if image not in metadata.art:
                metadata.art[image] = Proxy.Media(HTTP.Request(image), sort_order = y)
                Log.Info("sTHEGAMESDB.Update() - screenshots['%s']: '%s'" % (x, image))
                y += 1
            else:
                Log.Info("sTHEGAMESDB.Update() - screenshots['%s'] already in database: '%s'" % (x, image))
            
            x += 1
        
    except KeyError:
        Log.Info('screenshots not found')

    '''genres'''
    metadata.genres.clear()
    #genres --> genres
    jsonKey = 'genres'

    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            metadata.genres.add('Genre: ' + result[x]['name'])
            x += 1
            
    except KeyError:
        Log.Info('genres not found')
    
    #themes --> genres
    jsonKey = 'themes'

    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            metadata.genres.add('Theme: ' + result[x]['name'])
            x += 1
            
    except KeyError:
        Log.Info('themes not found')

    #game_modes --> genres
    jsonKey = 'game_modes'

    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            metadata.genres.add('Game Mode: ' + result[x]['name'])
            x += 1
            
    except KeyError:
        Log.Info('game modes not found')


    #player_perspectives --> genres
    jsonKey = 'player_perspectives'

    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        for key in result:
            metadata.genres.add('Player Perspective: ' + result[x]['name'])
            x += 1
            
    except KeyError:
        Log.Info('player perspectives not found')


    #multiplayer_modes --> genres
    jsonKey = 'multiplayer_modes'
    #fields = 'platform, campaigncoop, dropin, lancoop, offlinecoop, offlinecoopmax, offlinemax, onlinecoop, onlinecoopmax, onlinemax, splitscreen, splitscreenonline'

    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        x = 0
        y = 0
        while x < len(result):
            for key, value in result[x].items():
                if key == 'platform' and str(value) == gamePlatform: #try to find multiplayer modes that match the platform
                    y = x
                    break
            x += 1
        
        for key, value in result[y].items():
            if key != 'id' and key != 'platform':
                if value != False or value > 0:
                    if value == True:
                        metadata.genres.add(multiplayer_mode[key])
                    elif value > 0:
                        metadata.genres.add(multiplayer_mode[key] + str(value))
            
    except KeyError:
        Log.Info('multiplayer not found')
    
    #platform --> genre
    metadata.genres.add("Platform: %s" % (platformName))

    '''collections'''
    metadata.collections.clear()
    #collections
    jsonKey = 'collection'

    try:
        result = jsonGame[0][jsonKey]
        Log.Info(json.dumps(result, indent=2))

        tmp = result['name'] #only a single result is returned, no for loop needed
        Log.Info(tmp)
        if tmp not in metadata.collections:
            metadata.collections.add(tmp)
            
    except KeyError:
        Log.Info('collections not found')


    #franchises --> collections
    jsonKey = 'franchises'

    try:
        result = jsonGame[0][jsonKey]
        Log.Info(json.dumps(result, indent=2))
        try:
            x = 0
            for key in result:
                tmp = result[x]['name']
                if tmp not in metadata.collections:
                    metadata.collections.add(tmp)
                x += 1
        except KeyError:
            try: #sometimes it returns individual keys instead of a list... does it? need to verify
                tmp = result['name']
                Log.Info(tmp)
                if tmp not in metadata.collections:
                    metadata.collections.add(tmp)
            except KeyError:
                Log.Info('franchises not found')
    except KeyError:
        Log.Info('franchises not found')

    #platform --> collection
    if Prefs['bool_PlatformAsCollection'] == True:
        Log.Info('Setting platform as collection')
        metadata.collections.add("Platform: %s" % (platformName))
        Log.Info('Done setting platform as collection')

    '''extras'''
    #game_videos
    jsonKey = 'videos'

    resolutions = ['maxres', 'standard', 'high', 'medium', 'default']
    try:
        api_key = Prefs['str_YouTubeApiKey']
    except:
        api_key = archer_dict.dDefaultSettings['str_YouTubeApiKey']
    try:
        result = jsonGame[0][jsonKey]
        #Log.Info(json.dumps(result, indent=2))
        
        x = 0
        for key in result:
            try:
                igdb_name = result[x]['name']
                igdb_id = result[x]['video_id']
                video_by_id = get_youtube(igdb_id, api_key)
                video_details = video_by_id['items'][0]
                
                #print(video_details)
                #print(json.dumps(video_details, indent=2))
                
                video_url = 'https://www.youtube.com/watch?v=' + video_details['id']
                video_title = video_details['snippet']['title']
                video_thumbs = video_details['snippet']['thumbnails']
                #print(video_thumbs)
                
                for k, v in dict(video_thumbs).items(): #https://stackoverflow.com/a/33815594
                    if v is None:
                        del video_thumbs[k]
                #print(video_thumbs)
                
                video_thumbs = sorted(video_details['snippet']['thumbnails'].items(), key = lambda x: x[1]['width'], reverse=True) #https://www.geeksforgeeks.org/python-sort-nested-dictionary-by-key/
                #print(video_thumbs)
                
                video_thumb = video_thumbs[0][1]['url']
                Log.Info(video_url)
                Log.Info(video_title)
                Log.Info(video_thumb)
                
                extra_type = ''
                
                for extraType in Extras.type_order:
                    if extraType in igdb_name.lower() or extraType in video_title.lower():
                        extra_type = Extras.type_map[extraType]
                        Log.Info(extraType)
                        break

                if extra_type == '':
                    extra_type = OtherObject
                
                metadata.extras.add(extra_type(title=video_title, url=video_url, thumb=video_thumb))

            except IndexError: #not a youtube video
                pass
            x += 1

    except KeyError:
        Log.Info('extras not found')

    #not from game json
    '''actors'''
    #characters --> actors
    end_point = 'characters'
    fields = 'name, mug_shot.url, gender, species'
    sort = 'name'
    limit = 500
    byte_array = wrapper.api_request(
        end_point,
        'fields ' + fields + '; sort ' + sort + '; where games = (' + str(id) + '); limit ' + str(limit) + ';' #parenthesis around game id allows for characters to be in other games as well, instead of only in this one game
    )
    result = json.loads(byte_array)
    Log.Info(json.dumps(result, indent=2))
    
    metadata.roles.clear()
    
    images_first = [True, False]
    
    for bool in images_first:
        x= 0
        for key in result:
            
            try:
                testing = 'https:' + result[x]['mug_shot']['url'].replace('/t_thumb/', '/t_original/')
                has_image = True
            except KeyError:
                has_image = False
                pass
            
            if has_image == bool:
                #create the role object          
                role = metadata.roles.new()
                
                role.name = str(result[x]['name'])
                
                try:
                    gender = igdb_enums['character']['gender'][result[x]['gender']]
                except KeyError:
                    gender = None
                try:
                    species = igdb_enums['character']['species'][result[x]['species']]
                except KeyError:
                    species = None
                
                if gender != None and species != None:
                    role.role = '%s | %s' % (gender, species)
                elif gender != None:
                    role.role = '%s' % (gender)
                elif species != None:
                    role.role = '%s' % (species)

                try:
                    role.photo = 'https:' + result[x]['mug_shot']['url'].replace('/t_thumb/', '/t_original/')
                except KeyError:
                    pass
            
            x += 1

    '''for the future'''
    #possible path to resources directory ?
    #com.github.agents.reenignearcher.retroarcher://
    #com.github.agents.reenignearcher.retroarcher://Resources ???

    '''unused'''
    #clear these
    metadata.directors.clear()
    metadata.producers.clear()
