# -*- coding: utf-8 -*-
from nop import NOP


def plex_test(plex_builtin):
    try:
        exec(plex_builtin)
    except NameError:
        globals()[plex_builtin] = NOP()
    except:
        pass


plex_globals = [
    'Agent',
    'Core',
    'HTTP',
    'InterviewObject',
    'JSON',
    'Locale',
    'Log',
    'MessageContainer',
    'MetadataSearchResult',
    'OtherObject',
    'Prefs',
    'Proxy',
    'RSS',
    'TrailerObject',
    'Util'
    'XML',
    'YAML'
]
for name in plex_globals:
    plex_test(name)

plex_constants = {
    'CACHE_1MINUTE': 60,
    'CACHE_1HOUR': 3600,
    'CACHE_1DAY': 86400,
    'CACHE_1WEEK': 604800,
    'CACHE_1MONTH': 2592000
}
for name, value in plex_constants.items():
    plex_test(name)
