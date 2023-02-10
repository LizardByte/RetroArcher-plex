# -*- coding: utf-8 -*-

# standard imports
from datetime import datetime
import os
import sys

# plex debugging
try:
    import plexhints  # noqa: F401
except ImportError:
    pass
else:  # the code is running outside of Plex
    from plexhints import plexhints_setup, update_sys_path
    plexhints_setup()  # read the plugin plist file and determine if plexhints should use elevated policy or not
    update_sys_path()  # when running outside plex, append the path

    from plexhints.agent_kit import Agent, Media  # agent kit
    from plexhints.constant_kit import CACHE_1DAY  # constant kit
    from plexhints.decorator_kit import handler  # decorator kit
    from plexhints.extras_kit import InterviewObject, OtherObject, TrailerObject  # extras kit
    from plexhints.locale_kit import Locale  # locale kit
    from plexhints.log_kit import Log  # log kit
    from plexhints.model_kit import Movie  # model kit
    from plexhints.network_kit import HTTP  # network kit
    from plexhints.object_kit import MessageContainer, MetadataSearchResult, SearchResult  # object kit
    from plexhints.parse_kit import JSON  # parse kit
    from plexhints.prefs_kit import Prefs  # prefs kit
    from plexhints.proxy_kit import Proxy  # proxy kit
    from plexhints.resource_kit import Resource  # resource kit
    from plexhints.util_kit import String  # util kit


# imports from Libraries\Shared
import requests
from typing import Optional

# local imports
if sys.version_info.major < 3:
    from default_prefs import default_prefs
    import helpers
    import igdb_helpers
    from platform_map import platform_map
else:
    from .default_prefs import default_prefs
    from . import helpers
    from . import igdb_helpers
    from .platform_map import platform_map


# create the plugin menu under applications
@handler(prefix='/applications/retroarcher', name='RetroArcher')  # todo try different thumbs
def main():
    # since plex removed menu's nothing else is needed here
    pass


def ValidatePrefs():
    # type: () -> MessageContainer
    """
    Validate plug-in preferences.

    This function is called when the user modifies their preferences. The developer can check the newly provided values
    to ensure they are correct (e.g. attempting a login to validate a username and password), and optionally return a
    ``MessageContainer`` to display any error information to the user. See the archived Plex documentation
    `Predefined functions
    <https://web.archive.org/web/https://dev.plexapp.com/docs/channels/basics.html#predefined-functions>`_
    for more information.

    Returns
    -------
    MessageContainer
        Success or Error message dependeing on results of validation.

    Examples
    --------
    >>> ValidatePrefs()
    ...
    """
    error_message = ''  # start with a blank error message

    for key in default_prefs:
        try:
            Prefs[key]
        except KeyError:
            Log.Critical("Setting '%s' missing from 'DefaultPrefs.json'" % key)
            error_message += "Setting '%s' missing from 'DefaultPrefs.json'<br/>" % key
        else:
            # test all types except 'str_' as string cannot fail
            if key.startswith('int_'):
                try:
                    int(Prefs[key])
                except ValueError:
                    Log.Error("Setting '%s' must be an integer; Value '%s'" % (key, Prefs[key]))
                    error_message += "Setting '%s' must be an integer; Value '%s'<br/>" % (key, Prefs[key])
            elif key.startswith('bool_') or key.startswith('scanner_'):
                if Prefs[key] is not True and Prefs[key] is not False:
                    Log.Error("Setting '%s' must be True or False; Value '%s'" % (key, Prefs[key]))
                    error_message += "Setting '%s' must be True or False; Value '%s'<br/>" % (key, Prefs[key])
            if key.startswith('dir_'):
                if Prefs[key]:
                    if not os.path.isdir(Prefs[key]):
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
                            error_message += "Setting '%s' url returned a non 200 status code; Value '%s'<br/>" % (
                                key, Prefs[key])
                    except Exception as e:
                        Log.Error("Setting '%s' url returned an exception; Exception '%s'" % (key, e))
                        error_message += "Setting '%s' url returned an exception; Exception '%s'<br/>" % (key, e)
                else:
                    Log.Error("Setting '%s' url is blank; Value '%s'" % (key, Prefs[key]))
                    error_message += "Setting '%s' url is blank; Value '%s'<br/>" % (key, Prefs[key])

    if error_message != '':
        return MessageContainer(header='Error', message=error_message)
    else:
        Log.Info("DefaultPrefs.json is valid")
        return MessageContainer(header='Success', message='RetroArcher - Provided preference values are ok')


def SetRating(key, rating):
    # type: (str, float) -> None
    """
    This function is called when the user sets the rating of a metadata item returned by the plug-in. The `key`
    argument will be equal to the value of the item’s ``rating_key`` attribute. See the archived Plex documentation
    `Predefined functions
    <https://web.archive.org/web/https://dev.plexapp.com/docs/channels/basics.html#predefined-functions>`_
    for more information.

    Parameters
    ----------
    key : str
        This will be equal to the value of the item’s rating_key attribute.
    rating : float
        A float between 0 and 10 specifying the item’s rating.

    Examples
    --------
    >>> SetRating(key='123456', rating=8.8)
    ...
    """
    Log.Debug('User rated item (rating key: %s) with rating of %s' % (key, rating))
    # todo - possibly rate the item on IGDB


def Start():
    # type: () -> None
    """
    Start the plug-in.

    This function is called when the plug-in first starts. It can be used to perform extra initialisation tasks such as
    configuring the environment and setting default attributes. See the archived Plex documentation
    `Predefined functions
    <https://web.archive.org/web/https://dev.plexapp.com/docs/channels/basics.html#predefined-functions>`_
    for more information.

    Examples
    --------
    >>> Start()
    ...
    """
    # validate prefs
    prefs_valid = ValidatePrefs()
    if prefs_valid.header == 'Error':
        Log.Warn('RetroArcher Metadata agent preferences are not valid.')

    # set cache time
    HTTP.CacheTime = CACHE_1DAY

    Log.Debug('RetroArcher Metadata agent started.')


class RetroArcher(Agent.Movies):
    """
    Class representing the RetroArcher Plex Movie Agent.

    This class defines the metadata agent. See the archived Plex documentation
    `Defining an agent class
    <https://web.archive.org/web/https://dev.plexapp.com/docs/agents/basics.html#defining-an-agent-class>`_
    for more information.

    References
    ----------
    name : str
        A string defining the name of the agent for display in the GUI.
    languages : list
        A list of strings defining the languages supported by the agent. These values should be taken from the constants
        defined in the `Locale
        <https://web.archive.org/web/https://dev.plexapp.com/docs/api/localekit.html#module-Locale>`_
        API.
    primary_provider : bool
        A boolean value defining whether the agent is a primary metadata provider or not. Primary providers can be
        selected as the main source of metadata for a particular media type. If an agent is secondary
        (``primary_provider`` is set to ``False``) it will only be able to contribute to data provided by another
        primary agent.
    fallback_agent : Optional[str]
        A string containing the identifier of another agent to use as a fallback. If none of the matches returned by an
        agent are a close enough match to the given set of hints, this fallback agent will be called to attempt to find
        a better match.
    accepts_from : Optional[list]
        A list of strings containing the identifiers of agents that can contribute secondary data to primary data
        provided by this agent.
    contributes_to : Optional[list]
        A list of strings containing the identifiers of primary agents that the agent can contribute secondary data to.

    Methods
    -------
    search:
        Search for an item.
    update:
        Add or update metadata for an item.

    Examples
    --------
    >>> RetroArcher()
    ...
    """
    name = 'RetroArcher'
    languages = [
        Locale.Language.English
    ]
    primary_provider = True
    fallback_agent = False
    accepts_from = [
        'com.plexapp.agents.localmedia'
    ]
    contributes_to = None

    @staticmethod
    def search(results, media, lang, manual):
        # type: (SearchResult, Media.Movie, str, bool) -> Optional[SearchResult]
        """
        Search for an item.

        When the media server needs an agent to perform a search, it calls the agent’s ``search`` method. See the
        archived Plex documentation
        `Searching for results to provide matches for media
        <https://web.archive.org/web/https://dev.plexapp.com/docs/agents/search.html>`_
        for more information.

        Parameters
        ----------
        results : SearchResult
            An empty container that the developer should populate with potential matches.
        media : Media.Movie
            An object containing hints to be used when performing the search.
        lang : str
            A string identifying the user’s currently selected language. This will be one of the constants added to the
            agent’s ``languages`` attribute.
        manual : bool
            A boolean value identifying whether the search was issued automatically during scanning, or manually by the
            user (in order to fix an incorrect match).

        Returns
        -------
        Optional[SearchResult]
            The search result object, if the search was successful.

        Examples
        --------
        >>> RetroArcher().search(results=..., media=..., lang='en', manual=True)
        ...
        """
        Log.Debug('Searching with arguments: {results=%s, media=%s, lang=%s, manual=%s' %
                  (results, media, lang, manual))

        # media.name example = 'Driver You Are the Wheelman Usa V1 1'
        # media.title example = 'Driver - You Are the Wheelman (USA) (v1.1)'
        if not media.title:  # cannot search if no title
            Log.Error('Cannot search since "media.title" is empty: %s' % media.title)
            return

        if media.title.startswith('clear-cache'):
            Log.Info('Clearing HTTP cache.')
            HTTP.ClearCache()  # Clear Plex HTTP cache manually by searching a title named "clear-cache"

        # get the fullpath and media filename
        fullpath, media_filename = helpers.get_media_fullpath(media=media)

        # get the game version
        game_version = helpers.get_game_version(media_filename=media_filename)

        # get the game platform
        game_platform = helpers.get_game_platform(path=fullpath)

        # get the game name
        game_name = helpers.get_game_name(media=media, media_filename=media_filename)

        # get the igdb id
        platform_id = platform_map[game_platform]['systemIds']['igdb']

        # download platform data (including list of all games for that platform)
        # use plex JSON kit since they handle cache automatically
        platform_data = JSON.ObjectFromURL(url='https://db.lizardbyte.dev/platforms/%s.json' % platform_id)

        for game in platform_data['games']:
            result_name = game['name'].encode('utf-8')

            result_year = None
            try:
                for release_date in game['release_dates']:
                    try:
                        if release_date['platform'] == platform_id and\
                                (result_year is None or release_date['y'] < result_year):
                            result_year = release_date['y']
                    except KeyError:
                        Log.Info('Game {%s} is missing release year for one or more regions on platform {%s}. '
                                 'Contribute at https://www.igdb.com' % (result_name, game_platform))
            except KeyError:
                Log.Info('Game {%s} is missing release dates on platform {%s}. Contribute at https://www.igdb.com' %
                         (result_name, game_platform))

            result_score = int(String.LevenshteinRatio(first=game_name, second=result_name) * 100)

            try:
                # https://api-docs.igdb.com/#images
                result_thumb = 'https:%s' % game['cover']['url'].replace('/t_thumb/', '/t_cover_big/')
            except KeyError:
                result_thumb = None

            results.Append(MetadataSearchResult(
                id='{igdb-%s}{platform-%s}{%s}' % (game['id'], platform_id, game_version),
                # need many variables to build this in the update function
                # cannot do the following or all versions with igdb id get combined to a single entry
                # id = 'igdb-%s' % game['id],
                name=result_name,
                year=result_year,
                score=result_score,
                lang=lang,  # no lang to get from db
                thumb=result_thumb
            ))

        # sort the results first by year, then by score
        results.Sort(attr='year')
        results.Sort(attr='score', descending=True)
        return results

    @staticmethod
    def update(metadata, media, lang, force):
        # type: (Movie, Media.Movie, str, bool) -> Optional[Movie]
        """
        Update metadata for an item.

        Once an item has been successfully matched, it is added to the update queue. As the framework processes queued
        items, it calls the ``update`` method of the relevant agents. See the archived Plex documentation
        `Adding metadata to media
        <https://web.archive.org/web/https://dev.plexapp.com/docs/agents/update.html>`_
        for more information.

        Parameters
        ----------
        metadata : object
            A pre-initialized metadata object if this is the first time the item is being updated, or the existing
            metadata object if the item is being refreshed.
        media : object
            An object containing information about the media hierarchy in the database.
        lang : str
            A string identifying which language should be used for the metadata. This will be one of the constants
            defined in the agent’s ``languages`` attribute.
        force : bool
            A boolean value identifying whether the user forced a full refresh of the metadata. If this argument is
            ``True``, all metadata should be refreshed, regardless of whether it has been populated previously.

        Examples
        --------
        >>> RetroArcher().update(metadata=..., media=..., lang='en', force=True)
        ...
        """
        Log.Debug('Updating with arguments: {metadata=%s, media=%s, lang=%s, force=%s' %
                  (metadata, media, lang, force))

        # parameters
        id_list = helpers.get_list_of_substrings(string_subject=metadata.id, string1='{', string2='}')

        if 'igdb-' not in id_list[0] or 'platform-' not in id_list[1]:
            Log.Critical('This item has a problem with the id, please rematch the item to correct the issue. Exiting.')
            return

        igdb_id = int(id_list[0].split('-', 1)[-1])
        igdb_platform_id = int(id_list[1].split('-', 1)[-1])
        game_version = id_list[2]

        Log.Info('IGDB id: %s' % igdb_id)
        Log.Info('IGDB platform-id: %s' % igdb_platform_id)
        Log.Info('Game version: %s' % game_version)

        # get the platform_name from the platform_id
        platform_name = None
        for platform, platform_data in platform_map.items():
            if platform_data['systemIds']['igdb'] == igdb_platform_id:
                platform_name = platform
                Log.Info('Game platform: %s' % platform_name)
                break

        if not platform_name:  # platform not found
            Log.Critical('Platform name not found. Exiting.')
            return

        # download game data
        # use plex JSON kit since they handle cache automatically
        game = JSON.ObjectFromURL(url='https://db.lizardbyte.dev/games/%s.json' % igdb_id)

        # setup missing data list
        missing_details = []

        # title
        title = "%s [%s] %s" % (game['name'], platform_name, game_version)
        metadata.title = title.strip()
        Log.Info('Title: %s' % metadata.title)

        # summary
        try:
            metadata.summary = game['summary']
            Log.Info('Summary: %s' % metadata.summary)
        except KeyError:
            metadata.summary = None
            missing_details.append('summary')

        # critic rating
        try:
            metadata.rating = game['aggregated_rating'] / 10  # critic rating
            if metadata.rating >= 5.0:
                rating_image = 'rating_up.png'
            else:
                rating_image = 'rating_down.png'
            # todo - image doesn't work
            # metadata.rating_image = '/:/plugins/dev.lizardbyte.retroarcher-plex/resources/%s' % rating_image
            # metadata.rating_image = R(rating_image)
            metadata.rating_image = Resource.ExternalPath(rating_image)
            Log.Info('Rating: %s' % metadata.rating)
        except KeyError:
            metadata.rating = None
            metadata.rating_image = None
            missing_details.append('aggregated_rating')

        # audience rating
        try:
            metadata.audience_rating = game['rating'] / 10  # audience rating
            if metadata.audience_rating >= 5.0:
                rating_image = 'rating_up.png'
            else:
                rating_image = 'rating_down.png'
            # todo - image doesn't work
            # metadata.audience_rating_image = '/:/plugins/dev.lizardbyte.retroarcher-plex/resources/%s' % rating_image
            # metadata.audience_rating_image = R(rating_image)
            metadata.audience_rating_image = Resource.ExternalPath(rating_image)
            Log.Info('Audience rating: %s' % metadata.audience_rating)
        except KeyError:
            metadata.audience_rating = None
            metadata.audience_rating_image = None
            missing_details.append('rating')

        # studio
        try:
            for company in game['involved_companies']:
                if company['developer'] is True:
                    try:
                        metadata.studio = company['company']['name']
                        Log.Info('Studio: %s' % metadata.studio)
                        break
                    except KeyError:
                        missing_details.append('involved_companies/company_name')
        except KeyError:
            metadata.studio = None
            missing_details.append('involved_companies')

        # release_date
        # todo - add a way to get release date for specific version of game... for now just use earliest release date
        try:
            date = None
            for release_date in game['release_dates']:
                if release_date['platform'] == igdb_platform_id:
                    if date:
                        if release_date['date'] < date:  # use the earliest release date on that platform
                            metadata.year = release_date['y']
                            date = release_date['date']
                    else:
                        metadata.year = release_date['y']
                        date = release_date['date']
                    metadata.originally_available_at = datetime.utcfromtimestamp(date)

            if not date:
                try:
                    metadata.originally_available_at = datetime.utcfromtimestamp(game['first_release_date'])
                    metadata.year = datetime.utcfromtimestamp(game['first_release_date']).year
                except KeyError:
                    missing_details.append('first_release_date')

            Log.Info('Year: %s' % metadata.year)
            Log.Info('Originally available at: %s' % metadata.originally_available_at)
        except KeyError:
            metadata.year = None
            metadata.originally_available_at = None
            missing_details.append('release_dates/platform')

        # age ratings
        # use plex JSON kit since they handle cache automatically
        age_ratings_enums = JSON.ObjectFromURL(url='https://db.lizardbyte.dev/enums/age_ratings.json')

        preferred_age_rating_category_id = 1  # set default to ESRB
        for key, category in age_ratings_enums['category'].items():
            if category == Prefs['enum_PreferredRatingSystem']:
                preferred_age_rating_category_id = int(key)

        rating_test_order = range(1, len(age_ratings_enums['category']))  # test in IGDB order (ESRB, PEGI, etc, etc.)
        rating_test_order.remove(preferred_age_rating_category_id)  # remove the preferred rating category
        rating_test_order.insert(0, preferred_age_rating_category_id)  # add the preferred rating category at the start
        try:
            found_rating = False
            for category_id in rating_test_order:
                if found_rating:
                    break
                for age_rating in game['age_ratings']:
                    metadata.content_rating = age_ratings_enums['rating'][str(age_rating['rating'])]
                    metadata.content_rating_age = age_ratings_enums['rating_age'][str(age_rating['rating'])]

                    if age_rating['category'] == category_id:
                        found_rating = True  # break out of the upper loop
                        Log.Info('Content rating: %s' % metadata.content_rating)
                        Log.Info('Content rating age: %s' % metadata.content_rating_age)
                        break  # break out of the lower loop
        except KeyError:
            metadata.content_rating = None
            metadata.content_rating_age = None
            missing_details.append('age_ratings')

        # posters
        try:
            poster_image = 'https:%s' % game['cover']['url'].replace('/t_thumb/', '/t_original/')
            metadata.posters[id_list[0]] = Proxy.Media(HTTP.Request(poster_image), sort_order=0)
            Log.Info('Setting poster image to: %s' % poster_image)
        except KeyError:
            missing_details.append('cover')

        # art
        art_keys = ['artworks', 'screenshots']  # add both artworks and screenshots to metadata.arts
        art_index = 0
        for key in art_keys:
            try:
                for artwork in game[key]:
                    art_image = 'https:%s' % artwork['url'].replace('/t_thumb/', '/t_original/')
                    metadata.art[art_image] = Proxy.Media(HTTP.Request(art_image), sort_order=art_index)
                    Log.Info('Adding art image: %s' % art_image)
                    art_index += 1
            except KeyError:
                missing_details.append(key)

        # genres
        metadata.genres.clear()
        genre_keys = [
            ('Genre', 'genres'),
            ('Theme', 'themes'),
            ('Game Mode', 'game_modes'),
            ('Player Perspective', 'player_perspectives')
        ]
        for key in genre_keys:
            try:
                for genre in game[key[1]]:
                    metadata.genres.add('%s: %s' % (key[0], genre['name']))
            except KeyError:
                missing_details.append(key[1])

        # genres (multiplayer modes)
        try:
            for version in game['multiplayer_modes']:  # this is a list
                if version['platform'] == igdb_platform_id:
                    for mode in version:  # this is a dict
                        try:
                            if version[mode] is False:
                                pass  # skip these
                            elif version[mode] is True:
                                metadata.genres.add('Multiplayer Mode: %s' % igdb_helpers.multiplayer_mode[mode])
                            elif version[mode] > 0:
                                metadata.genres.add('Multiplayer Mode: %s: %s' %
                                                    (igdb_helpers.multiplayer_mode[mode], version[mode]))
                        except KeyError:
                            pass  # skip any items not in our dictionary
        except KeyError:
            missing_details.append('multiplayer_modes')

        # genres (platform)
        metadata.genres.add("Platform: %s" % platform_name)

        Log.Info('Genres: %s' % metadata.genres)

        # collections
        metadata.collections.clear()
        try:
            metadata.collections.add(game['collection']['name'])
        except KeyError:
            missing_details.append('collection')

        # collections (franchises)
        try:
            for franchise in game['franchises']:  # this is a list
                if franchise['name'] not in metadata.collections:
                    metadata.collections.add(franchise['name'])
        except KeyError:
            missing_details.append('franchises')

        # collection (platform)
        if Prefs['bool_PlatformAsCollection'] is True:
            metadata.collections.add("Platform: %s" % platform_name)

        Log.Info('Collections: %s' % metadata.collections)

        # extras / videos
        extra_type_map = {
            'trailer': TrailerObject,
            'teaser': TrailerObject,
            'gameplay': OtherObject,
            'interview': InterviewObject
        }

        # todo - clear existing extra objects

        try:
            for video in game['videos']:
                igdb_video_name = video['name']

                video_data = JSON.ObjectFromURL(url='https://db.lizardbyte.dev/videos/%s.json' % video['video_id'])

                video_url = 'https://www.youtube.com/watch?v=%s' % video_data['id']
                video_title = video_data['snippet']['title']
                video_thumbs = video_data['snippet']['thumbnails']

                # iterate over a copy of the original dictionary, while modifying the original
                # https://stackoverflow.com/a/33815594
                for thumb_key, thumb_data in dict(video_thumbs).items():
                    if thumb_data is None:
                        del video_thumbs[thumb_key]

                # sort the thumbs by size
                # https://www.geeksforgeeks.org/python-sort-nested-dictionary-by-key/
                video_thumbs = sorted(video_data['snippet']['thumbnails'].items(), key=lambda x: x[1]['width'],
                                      reverse=True)

                video_thumb = video_thumbs[0][-1]['url']

                extra_method = OtherObject  # set the default type, then try to match a better type
                for extra_type in extra_type_map:
                    if extra_type in igdb_video_name.lower() or extra_type in video_title.lower():
                        extra_method = extra_type_map[extra_type]
                        break

                metadata.extras.add(extra_method(title=video_title, url=video_url, thumb=video_thumb))
                Log.Info('Adding extra: %s' % video_title)
                Log.Info('Extra video url: %s' % video_url)
        except KeyError:
            missing_details.append('videos')

        # actors (characters)
        character_enums = JSON.ObjectFromURL(url='https://db.lizardbyte.dev/enums/characters.json')

        metadata.roles.clear()
        images_first = [True, False]
        try:
            for image_order in images_first:
                for character in game['characters']:
                    try:
                        character['mug_shot']['url']
                    except KeyError:
                        has_image = False
                    else:
                        has_image = True

                    if has_image == image_order:
                        # create the role object
                        role = metadata.roles.new()

                        role.name = character['name']

                        role.photo = None  # reset the image

                        try:
                            gender = character_enums['gender'][str(character['gender'])]
                        except KeyError:
                            gender = None
                        try:
                            species = character_enums['species'][str(character['species'])]
                        except KeyError:
                            species = None

                        if gender and species:
                            role.role = '%s | %s' % (gender, species)
                        elif gender:
                            role.role = '%s' % gender
                        elif species:
                            role.role = '%s' % species

                        Log.Info('Adding character named "%s" as "%s"' % (role.name, role.role))

                        if has_image:
                            role.photo = 'https:%s' % character['mug_shot']['url'].replace('/t_thumb/', '/t_original/')
                            Log.Info('Set character image to: %s' % role.photo)
        except KeyError:
            missing_details.append('characters')

        # clear these
        metadata.directors.clear()
        metadata.producers.clear()

        # log the missing data
        if missing_details:
            Log.Info('Game {%s} is missing the following metadata: %s. '
                     'Contribute at https://www.igdb.com' % (metadata.title, missing_details))

        return metadata
