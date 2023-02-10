# standard imports
import os
from future.moves.urllib.parse import quote

# lib imports
from plexhints.agent_kit import Media
from plexhints.object_kit import SearchResult

from plexhints.model_kit import Movie

# local imports
from Code import RetroArcher

# prep agent
agent = RetroArcher()
media = Media.Movie()

# prep search method
path = os.path.join('E:\\', 'AppData', 'Plex Media Server', 'Plug-in Support', 'Data',
                    'com.github.agents.retroarcher.retroarcher', 'media', 'Games', 'Nintendo 64',
                    '007 - GoldenEye (USA).mp4')

media.id = 123456  # fake rating key
media.title = '007 - GoldenEye (USA)'
media.name = '007 Goldeneye Usa'
media.year = -1
media.filename = quote(s=path).replace('.', '%2E')  # url quote, plus manual quoting of period

results = agent.search(results=SearchResult(), media=media, lang='en', manual=False)

# prep update method
metadata = Movie()

for result in results.__items__:
    print(result.__dict__)

    metadata.id = result.__dict__['id']
    metadata.title = result.__dict__['name']
    metadata.type = 'Movie'
    break  # 'SearchResult' object does not support indexing

update = agent.update(metadata=metadata, media=media, lang='en', force=True)
