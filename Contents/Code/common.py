# plex debugging
import sys
if 'plexscripthost' not in sys.executable.lower():
    from plexagents.builtins import *

# local imports
import archer_dict
import sIGDB
import sThemeSongs

class sites:
    sName = [['IGDB']]
    sPrefix = [['igdb-']]
    sSearchMax = [500]

dSites = {
    0 : {
        'sName' : 'IGDB',
        'sPrefix' : 'igdb-',
        'sSearchMax' : 500
        }
}

########################################################################################################################    
def GetListOfSubstrings(stringSubject,string1,string2):
    MyList = []
    intstart=0
    strlength=len(stringSubject)
    continueloop = 1
    while(intstart < strlength and continueloop == 1):
        intindex1=stringSubject.find(string1,intstart)
        if(intindex1 != -1): #The substring was found, lets proceed
            intindex1 = intindex1+len(string1)
            intindex2 = stringSubject.find(string2,intindex1)
            if(intindex2 != -1):
                subsequence=stringSubject[intindex1:intindex2]
                MyList.append(subsequence)
                intstart=intindex2+len(string2)
            else:
                continueloop=0
        else:
            continueloop=0
    return MyList
########################################################################################################################
def double_space_replace(string):
    while '  ' in string:
        string = string.replace('  ', '')
    return string
########################################################################################################################
def Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform):
    site_name = Prefs['enum_SearchSite']
    Log.Info("common.Search() - Using site: '%s'" % (site_name))
    site_index = archer_dict.dict_enum_agent_map['SearchSite'][site_name.lower()]
    Log.Info("common.Search() - Using site index: '%s'" % (site_index))
    Log.Info("common.Search() - Game Name: '%s'" % (game_name))
    Log.Info("common.Search() - Game Platform: '%s'" % (game_platform))
    game_platform_id = archer_dict.dPlatformMapping[game_platform]['systemIds'][site_name.lower()]
    Log.Info("common.Search() - Game Platform ID: '%s'" % (game_platform_id))
    Log.Info("common.Search() - Movie: '%s'" % (movie))
    if site_index == 0:
        sIGDB.Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform_id, site_index)
    elif site_index == 1:
        Log.Info("common.Search() - Specified search database is not available yet: '%s'" % (game_name))
        #sTHEGAMESDB.Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform_id, site_index)
    elif site_index == 2:
        Log.Info("common.Search() - Specified search database is not available yet: '%s'" % (game_name))
        #sSCREENSCRAPER.Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform_id, site_index)
    elif site_index == 3:
        Log.Info("common.Search() - Specified search database is not available yet: '%s'" % (game_name))
        #sLAUNCHBOX.Search(self, results, media, lang, manual, movie, game_name, game_version, game_platform_id, site_index)
    else:
        Log.Info("common.Search() - Error finding site_index from preferences: '%s'" % (game_name))
########################################################################################################################
def Update(self, metadata, media, lang, force, movie, game):
    site_index = game[0]
    if site_index == 0:
        sIGDB.Update(self, metadata, media, lang, force, movie, game)
    elif site_index == 1:
        Log.Info("common.Update() - Specified database is not available yet: '%s'" % (metadata.id))
        #sTHEGAMESDB.Update(self, metadata, media, lang, force, movie, game)
    elif site_index == 2:
        Log.Info("common.Update() - Specified database is not available yet: '%s'" % (metadata.id))
        #sSCREENSCRAPER.Update(self, metadata, media, lang, force, movie, game)
    elif site_index == 3:
        Log.Info("common.Update() - Specified database is not available yet: '%s'" % (metadata.id))
        #sLAUNCHBOX.Update(self, metadata, media, lang, force, movie, game)
    else:
        Log.Info("common.Update() - No site found for metadata.id: '%s'" % (metadata.id))
########################################################################################################################
def Themes(self, metadata, media, lang, force, movie, game):
    if Prefs['enum_ThemesSource'] == 'Local':
        sThemeSongs.Themes(self, metadata, media, lang, force, movie, game)
    else:
        Log.Info("common.Themes() - No theme song database selected in options")
########################################################################################################################
def platformPath(fullpath):
    dirLength = len(splitall(fullpath))
    dirPath = os.path.dirname(fullpath)
    dirName = os.path.basename(dirPath)
    #Log.Info(dirLength)
    
    x =  0
    while x < dirLength:
        for key, value in archer_dict.dPlatformMapping.items():
            #Log.Info(value[0])
            
            #if dirName == value[0]:
            if dirName == key:
                x = dirLength
                game_platform = dirName
                break
        dirPath = os.path.dirname(dirPath)
        dirName = os.path.basename(dirPath)
        x += 1
    return game_platform
########################################################################################################################
def splitall(path): #https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s16.html
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

