# -*- coding: utf-8 -*-
import os
import sys

# imports from Libraries\Shared
try:
    # these imports will succeed when running in plex
    import requests
    import urllib
except ImportError:
    # when running outside of plex we must append the path
    sys.path.append(os.path.join('Contents', 'Libraries', 'Shared'))
    import requests
    import urllib

# plex debugging
if 'plexscripthost' not in sys.executable.lower():
    from plexagents.builtins import *

# local imports
import archer_dict
import common


def ValidatePrefs():
    """Returns message as response when save request is made"""

    error_message = ''

    try:
        for key in archer_dict.dDefaultSettings:
            Prefs[key]
            Log.Debug(key)
            Log.Debug(Prefs[key])
    except:
        Log.Error("Setting '%s' missing from 'DefaultPrefs.json'" % key)
        error_message += "Setting '%s' missing from 'DefaultPrefs.json'<br/>" % key

    for key in archer_dict.dDefaultSettings:
        if key.startswith('int_'):
            try:
                int(Prefs[key])
            except:
                Log.Error("Setting '%s' must be an integer; Value '%s'" % (key, Prefs[key]))
                error_message += "Setting '%s' must be an integer; Value '%s'<br/>" % (key, Prefs[key])
        elif key.startswith('bool_') or key.startswith('scanner_'):
            if Prefs[key] != True and Prefs[key] != False:
                Log.Error("Setting '%s' must be True or False; Value '%s'" % (key, Prefs[key]))
                error_message += "Setting '%s' must be True or False; Value '%s'<br/>" % (key, Prefs[key])
        if key.startswith('str_'):
            try:
                str(Prefs[key])
            except:
                Log.Error("Setting '%s' must be a string; Value '%s'" % (key, Prefs[key]))
                error_message += "Setting '%s' must be a string; Value '%s'<br/>" % (key, Prefs[key])
        if key.startswith('dir_'):
            dir = Prefs[key]
            if dir:
                if not os.path.isdir(dir):
                    Log.Error("Setting '%s' directory does not exist; Value '%s'" % (key, Prefs[key]))
                    error_message += "Setting '%s' directory does not exist; Value '%s'<br/>" % (key, Prefs[key])
            else:
                Log.Error("Setting '%s' directory is blank; Value '%s'" % (key, Prefs[key]))
                error_message += "Setting '%s' directory is blank; Value '%s'<br/>" % (key, Prefs[key])
        if key.startswith('url_'):
            url = Prefs[key]
            if url:
                try:
                    status_code = requests.get(url).status_code
                    if status_code != 200:
                        Log.Error("Setting '%s' url returned a non 200 status code; Value '%s'" % (key, Prefs[key]))
                        error_message += "Setting '%s' url returned a non 200 status code; Value '%s'<br/>" % (key, Prefs[key])
                except Exception as e:
                    Log.Error("Setting '%s' url returned an exception; Exception '%s'" % (key, e))
                    error_message += "Setting '%s' url returned an exception; Exception '%s'<br/>" % (key, e)
            else:
                Log.Error("Setting '%s' url is blank; Value '%s'" % (key, Prefs[key]))
                error_message += "Setting '%s' url is blank; Value '%s'<br/>" % (key, Prefs[key])

    if error_message != '':
        return MessageContainer ('Error', error_message)
    else:
        Log.Info ("DefaultPrefs.json is valid")
        return MessageContainer ('Success', 'RetroArcher - Provided preference values are ok')


def Start():
  msgContainer = ValidatePrefs();
  if msgContainer.header == 'Error': return
  Log.Debug('### RetroArcher Metadata Agent Started ##############################################################################################################')
  HTTP.CacheTime = CACHE_1HOUR * 24


class RetroArcherCommonAgent:

    ### Search ######################################################################################################################################################
    def Search(self, results, media, lang, manual, movie):
        Log.Debug("=== Search - Begin - ================================================================================================")
        orig_title = ( media.title if movie else media.show )
        try:    orig_title = orig_title.encode('utf-8')  # NEEDS UTF-8
        except: Log("UTF-8 encode issue")
        if not orig_title:  return
        if orig_title.startswith("clear-cache"):   HTTP.ClearCache()  ### Clear Plex http cache manually by searching a serie named "clear-cache" ###
        Log.Info("search() - Title: '%s', name: '%s', filename: '%s', manual:'%s'" % (orig_title, media.name, media.filename, str(manual)))  #if media.filename is not None: filename = String.Unquote(media.filename) #auto match only
        Log.Info("search() - Orig_Title: '%s', Name: '%s', Year: '%s', Filename: '%s', Manual:'%s'" % (orig_title, media.name, media.year, media.filename, str(manual)))  #if media.filename is not None: filename = String.Unquote(media.filename) #auto match only

        fullpath = media.items[0].parts[0].file
        Log.Info(fullpath)

        game_name_full = os.path.basename(fullpath) #the file name
        Log.Info(game_name_full)

        game_version = game_name_full.rsplit('.', 1)[0].split('(', 1)[-1].strip()
        if game_version != game_name_full.rsplit('.', 1)[0]:
            game_version = '(' + game_version
        else:
            game_version = ''
        Log.Info(game_version)

        game_platform = common.platformPath(fullpath)
        Log.Info(game_platform)

        if media.filename is not None: #do this when first initiating a fix match or automatch
            #fullpath = urllib.unquote(media.filename) #the full path of the video file... this only works on auto search

            game_name = game_name_full.rsplit('.', 1)[0].split('(', 1)[0].strip()

        else: #do this when perfoming a manual search
            game_name = media.name

        Log.Info(game_name)

        Log.Info("__init__.Search() - Fullpath: '%s' Filename: '%s', Title: '%s', Version: '%s', Platform: '%s'" % (fullpath, game_name_full, game_name, game_version, game_platform))

        common.Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform)

        #sort the results by score
        results.Sort('score', descending=True)

    ### Update the Metadata ##################################################################################################################################
    def Update(self, metadata, media, lang, force, movie):
        Log.Debug('--- Update Begin -------------------------------------------------------------------------------------------')

        '''
        Log.Info(media)
        Log.Info(type(media))
        Log.Info(media.items)
        Log.Info(type(media.items))
        Log.Info(len(media.items))
        x = 0
        while x < len(media.items):
            Log.Info(media.items[x].parts)
            Log.Info(len(media.items[x].parts))
            y = 0
            while y < len(media.items[x].parts):
                Log.Info(media.items[x].parts[y])
                Log.Info(media.items[x].parts[y].file)
                Log.Info(media.items[x].parts[y].hash)
                Log.Info(media.items[x].parts[y].hash[0])
                Log.Info(media.items[x].parts[y].hash[1:])
                Log.Info(media.items[x].parts[y].id)
                y +=1
            x +=1
        '''

        rating_key = media.id # rating key whoop whoop!!!
        Log.Info(rating_key)

        fullpath = media.items[0].parts[0].file
        Log.Info(fullpath)
        Log.Info(type(fullpath))

        game_name_full = os.path.basename(fullpath) #the file name
        Log.Info(game_name_full)

        game_name = game_name_full.rsplit('.',1)[0] #the file name
        Log.Info(game_name)

        game_version = game_name_full.rsplit('.', 1)[0].split('(', 1)[-1].strip()
        if game_version != game_name_full.rsplit('.', 1)[0]:
            game_version = '(' + game_version
        else:
            game_version = ''
        Log.Info(game_version)

        game_platform = common.platformPath(fullpath)
        Log.Info(game_platform)

        #parameters
        full_id = common.GetListOfSubstrings( metadata.id, '{', '}' )
        #game_name = full_id[0]
        #game_version = full_id[1]
        #game_platform = full_id[2]
        site_id = full_id[3]
        site_short = site_id.split('-', 1)[0]
        site_index = archer_dict.dSiteShortNames2[site_short]
        id = site_id.split('-', 1)[1]

        #can't do this or all versions with same igdb id get combined
        #site_short = metadata.id.split('-', 1)[0]
        #site_index = archer_dict.dSiteShortNames2[site_short]
        #id = metadata.id.split('-', 1)[1]

        Log.Info("init.Update() - site_index: '%s', site_short: '%s', id: '%s'" % (site_index, site_short, id))
        Log.Info("init.Update() - game_platform: '%s'" % (game_platform))

        game = [site_index, id, game_name, game_version, game_platform]

        common.Update(self, metadata, media, lang, force, movie, game)

        if Prefs['enum_ThemesSource'] != 'none':
            common.Themes(self, metadata, media, lang, force, movie, game)

### Agent declaration ###############################################################################################################################################
class RetroArcher(Agent.Movies, RetroArcherCommonAgent):
    name, primary_provider, fallback_agent, contributes_to, languages, accepts_from = ('RetroArcher', True, False, None, [Locale.Language.English,], ['com.plexapp.agents.localmedia'] ) #, 'com.plexapp.agents.opensubtitles'
    def search(self, results, media, lang, manual): self.Search(results, media, lang, manual, True)
    def update(self, metadata, media, lang, force): self.Update(metadata, media, lang, force, True)