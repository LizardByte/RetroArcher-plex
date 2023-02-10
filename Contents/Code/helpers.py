# -*- coding: utf-8 -*-

# standard imports
import os
import sys
from typing import List, Optional, Tuple


# plex debugging
try:
    import plexhints  # noqa: F401
except ImportError:
    pass
else:  # the code is running outside of Plex
    from plexhints.log_kit import Log
    from plexhints.agent_kit import Media
    from plexhints.util_kit import String

# local imports
if sys.version_info.major < 3:
    from platform_map import platform_map
else:
    from .platform_map import platform_map


def get_list_of_substrings(string_subject, string1, string2):
    # type: (str, str, str) -> List
    """
    Get list of strings between two strings.

    Parameters
    ----------
    string_subject : str
        The string to search.
    string1 : str
        Search start string.
    string2 : str
        Search end string.

    Returns
    -------
    List
        List of strings.

    Examples
    --------
    >>> get_list_of_substrings(string_subject='{test1}{test2}{test3}', string1='{', string2='}')
    ['test1', 'test2', 'test3']
    """
    str_list = []
    int_start = 0
    continue_loop = True
    while int_start < len(string_subject) and continue_loop:
        int_index1 = string_subject.find(string1, int_start)
        if int_index1 != -1:  # The substring was found, lets proceed
            int_index1 = int_index1 + len(string1)
            int_index2 = string_subject.find(string2, int_index1)
            if int_index2 != -1:
                subsequence = string_subject[int_index1:int_index2]
                str_list.append(subsequence)
                int_start = int_index2 + len(string2)
            else:
                continue_loop = False
        else:
            continue_loop = False
    return str_list


def get_media_fullpath(media):
    # type: (Media.Movie) -> Tuple[str, str]
    """
    Get the fullpath of the plex media item.

    Parameters
    ----------
    media : Media.Movie
        The media item passed in from plex.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the fullpath and media_filename

    Examples
    --------
    >>> get_media_fullpath(media=media)
    ('...', '...')
    """
    try:
        # media.filename is only available on auto match so get the path from the part
        fullpath = media.items[0].parts[0].file
    except AttributeError:  # since it doesn't work in plexhints yet
        fullpath = String.Unquote(media.filename)
    Log.Info('Fullpath: %s' % fullpath)

    media_filename = os.path.basename(fullpath)  # the file name
    Log.Info('Filename: %s' % media_filename)

    return fullpath, media_filename


def get_game_version(media_filename):
    # type: (str) -> str
    """
    Get the game version from the given media_filename.

    Parameters
    ----------
    media_filename : str
        The filename of the media object representing the game.

    Returns
    -------
    str
        The version of the game.

    Examples
    --------
    >>> get_game_version(media_filename='007 - GoldenEye (USA).mp4')
    '(USA)'
    """
    game_version = ''
    ver_seps = [('(', ')'), ('[', ']')]

    for sep in ver_seps:
        game_version = media_filename.rsplit('.', 1)[0].split(sep[0], 1)[-1].split(sep[-1], 1)[0].strip()
        if game_version != media_filename.rsplit('.', 1)[0]:
            # add brackets back in event there are multiple tags, e.g. (USA) (Demo) (Kiosk)
            game_version = '%s%s%s' % (sep[0], game_version, sep[-1])
            break

    Log.Info('Game Version: %s' % game_version)
    return game_version


def get_game_platform(path):
    # type: (str) -> Optional[str]
    """
    Get the game platform from the given path.

    Parameters
    ----------
    path : str
        The path of the media object representing the game.

    Returns
    -------
    str
        The platform of the game.

    Examples
    --------
    >>> get_game_platform(path='.../media/Nintendo 64/007 - GoldenEye (USA).mp4')
    'Nintendo 64'
    """
    platform = os.path.split(os.path.dirname(path))[-1]

    for key in platform_map:
        if platform == key:
            Log.Info('Game Platform: %s' % platform)
            return platform

    Log.Error('Game platform not found.')
    return


def get_game_name(media, media_filename):
    # type: (Media.Movie, str) -> str
    """
    Get the game name from the given media object or media_filename.

    Parameters
    ----------
    media : Media.Movie
        Media object provided by plex framework.
    media_filename : str
        The filename of the media object representing the game.

    Returns
    -------
    str
        The game name.

    Examples
    --------
    >>> get_game_name(media=media, media_filename='007 - GoldenEye (USA).mp4')
    '007 - GoldenEye'
    """
    clear_str = 'clear-cache'

    game_name = media_filename.rsplit('.', 1)[0].split('(', 1)[0].strip()  # for update or auto search

    try:
        media.filename  # auto match or when first initiating a fix match
    except AttributeError:  # do this when updating metadata
        pass  # use the game_name already defined
    else:  # do this when searching
        if not media.filename:  # for manual search this value will be ``None``
            game_name = media.name.strip()  # overwrite the game_name with the search term

            # remove the "clear-cache" from start of name
            if game_name.startswith(clear_str):
                game_name = game_name[len(clear_str):].strip()

    Log.Info('Game Name: %s' % game_name)
    return game_name
