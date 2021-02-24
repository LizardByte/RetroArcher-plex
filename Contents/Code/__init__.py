# -*- coding: utf-8 -*-

### Imports ###
import os
import urllib

# Archer Modules #
import archer_dict
import common

def ValidatePrefs(): #     a = sum(getattr(t, name, 0) for name in "xyz")
    
    MessageContainer ('Test', 'This message is a test')
    
    try:
        [Prefs[key] for key in archer_dict.dDefaultSettings]
    except:
        Log.Error("DefaultPrefs.json invalid" )
        return MessageContainer ('Error', "Value '%s' missing from 'DefaultPrefs.json', update it" % key)
    else:
        Log.Info ("DefaultPrefs.json is valid")
        return MessageContainer ('Success', 'RetroArcher - Provided preference values are ok')
    
def Start():
  msgContainer = ValidatePrefs();
  if msgContainer.header == 'Error': return
  Log.Debug('### RetroArcher Metadata Agent Started ##############################################################################################################')
  HTTP.CacheTime          = CACHE_1HOUR * 24

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
        
        if Prefs['sThemesSource'] != 'none':
            common.Themes(self, metadata, media, lang, force, movie, game)

### Agent declaration ###############################################################################################################################################
class RetroArcher(Agent.Movies, RetroArcherCommonAgent):
    name, primary_provider, fallback_agent, contributes_to, languages, accepts_from = ('RetroArcher', True, False, None, [Locale.Language.English,], ['com.plexapp.agents.localmedia'] ) #, 'com.plexapp.agents.opensubtitles'
    def search(self, results, media, lang, manual): self.Search(results, media, lang, manual, True)
    def update(self, metadata, media, lang, force): self.Update(metadata, media, lang, force, True)