```
TSEMAGT | Metadata Model Classes | Description - Source: http://dev.plexapp.com/docs/agents/models.html 
------- | ---------------------- | --------------------------------------------------------------------------------------------------
X______ | class TV_Show          | Represents a TV show, or the top -level of other episodic content.
_X_____ | class Season           | Represents a season of a TV show.
__X____ | class Episode          | Represents an episode of a TV show or other episodic content. 
___X___ | class Movie            | Represents a movie (e.g. a theatrical release, independent film, home movie, etc.)
____X__ | class Album            | Represents a music album.
_____X_ | class Artist           | Represents an artist or group.
______X | Track                  | Represents an audio track (e.g. music, audiobook, podcast, etc.)   
------- | ---------------------- | --------------------------------------------------------------------------------------------------
X_XXXX_ | title                  | A string specifying the title.
XXXXXX_ | summary                | A string specifying the summary.
X_XXX__ | originally_available_at| A date object specifying the movie/episode’s original release date.
X_XXXX_ | rating                 | A float between 0 and 10 specifying the movie/episode’s rating.
X_XXXX_ | rating_image           | A string specifying the rating image (similar to imdb/rotten tomatoes images)... how to make it work?
uuuXuuu | audience_rating        | A float between 0 and 10 specifying the movie/episode’s rating.
uuuXuuu | audience_rating_image  | A string specifying the audience rating image (similar to rotten tomatoes images)... how to make it work?
X__XX__ | studio                 | A string specifying the studio.
X__XX__ | countries              | A set of strings specifying the countries involved in the production of the movie.
X__X___ | duration               | An integer specifying the duration of the movie, in milliseconds.
X__XXX_ | genres                 | A set of strings specifying the movie’s genre.
X__XXX_ | tags                   | A set of strings specifying the movie’s tags.
X__XXX_ | collections            | A set of strings specifying the movie’s collections.
uuuXuuu | similar                | A set of strings specifying similar items.
X__X___ | content_rating         | A string specifying the movie’s content rating.
__X____ | absolute_index         | An integer specifying the absolute index of the episode within the entire series.
______X | name                   | A string specifying the track’s name.
_X_____ | episodes               | A map of Episode objects.
____X__ | tracks                 | A map of Track objects.
------- | ---------------------- | ---------------------------------------------------------------------------------------------------
__XX___ | roles                  | A set of strings specifying the actors and actresses. (name, role, photo)
__XX___ | writers                | A set of strings specifying the writers. (name, role, photo)
__XX___ | directors              | A set of strings specifying the directors. (name, role, photo)
__XXX__ | producers              | A set of strings specifying the producers. (name, role, photo)
------- | ---------------------- | ---------------------------------------------------------------------------------------------------
__XX___ | chapters               | A set of strings specifying the chapters for 'title'. Time in milliseconds for start and end time. (title, start_time_offset, end_time_offset)
__XX___ | reviews                | A set of strings specifying the reviews. (source, image, link, author, text)... how to get image to work?
------- | ---------------------- | ---------------------------------------------------------------------------------------------------
___X___ | year                   | An integer specifying the movie’s release year.
___X___ | content_rating_age     | A string specifying the minumum age for viewers of the movie.
___X___ | trivia                 | A string containing trivia about the movie.
___X___ | quotes                 | A string containing memorable quotes from the movie.
___XX__ | original_title         | A string specifying the original title.
___X___ | tagline                | A string specifying the tagline.
------- | ---------------------- | ---------------------------------------------------------------------------------------------------
X__X_X_ | art                    | A container of proxy objects representing the movie’s background art.
XX_XXX_ | posters                | A container of proxy objects representing the movie’s posters.
XX_____ | banners                | A container of proxy objects representing the season’s banner images.
X__X_X_ | themes                 | A container of proxy objects representing the movie’s theme music.
__X____ | thumbs                 | A container of proxy objects representing the episode’s thumbnail images.
------- | ---------------------- | ---------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
Metadata source                             | pornhub.com              | perfectgonzo.com          |
--------------------------------------------|--------------------------|---------------------------|
Metadata Archer tags                        | ph                       | pg                        |
----------------------------------------------------------------------------------------------------
Movie   - title                             | Yes                      | ?                         |
Movie   - summary                           | Yes                      | ?                         |
Movie   - originally_available_at           | Yes                      | ?                         |
Movie   - rating                            | Yes (remove one)         | ?                         |
Movie   - rating_image                      | ?                        | ?                         |
Movie   - audience_rating                   | Yes (remove one)         | ?                         |
Movie   - audience_rating_image             | ?                        | ?                         |
Movie   - studio                            | Yes                      | ?                         |
Movie   - countries                         | ?                        | ?                         |
Movie   - duration                          | Yes                      | ?                         |
Movie   - genres                            | Yes                      | ?                         |
Movie   - tags                              | Pending                  | ?                         |
Movie   - collections                       | Yes                      | ?                         |
Movie   - similar                           | Yes                      | ?                         |
Movie   - content_rating                    | Yes                      | ?                         |
Movie   - roles                             | Yes                      | ?                         |
Movie   - writers                           | No                       | ?                         |
Movie   - directors                         | Yes                      | ?                         |
Movie   - producers                         | Yes                      | ?                         |
Movie   - chapters                          | Yes                      | ?                         |
Movie   - reviews                           | Yes                      | ?                         |
Movie   - art                               | Yes (video thumbnail)    | ?                         |
Movie   - posters                           | Yes (video thumbnail)    | ?                         |
Movie   - banners                           | No                       | ?                         |
Movie   - themes                            | No                       | ?                         |
----------------------------------------------------------------------------------------------------
TV_Show - Serie   - title                   | ?                        | ?                         |
TV_Show - Serie   - summary                 | ?                        | ?                         |
TV_Show - Serie   - originally_available_at | ?                        | ?                         |
TV_Show - Serie   - rating                  | ?                        | ?                         |
TV_Show - Serie   - studio                  | ?                        | ?                         |
TV_Show - Serie   - countries               | ?                        | ?                         |
TV_Show - Serie   - duration                | ?                        | ?                         |
TV_Show - Serie   - genres                  | ?                        | ?                         |
TV_Show - Serie   - tags                    | ?                        | ?                         |
TV_Show - Serie   - collections             | ?                        | ?                         |
TV_Show - Serie   - content_rating          | ?                        | ?                         |
TV_Show - Serie   - art                     | ?                        | ?                         |
TV_Show - Serie   - posters                 | ?                        | ?                         |
TV_Show - Serie   - banners                 | ?                        | ?                         |
TV_Show - Serie   - themes                  | ?                        | ?                         |
----------------------------------------------------------------------------------------------------
TV_Show - Season  - summary                 | ?                        | ?                         |
TV_Show - Season  - posters                 | ?                        | ?                         |
TV_Show - Season  - banners                 | ?                        | ?                         |
----------------------------------------------------------------------------------------------------
TV_Show - Episode - title                   | ?                        | ?                         |
TV_Show - Episode - summary                 | ?                        | ?                         |
TV_Show - Episode - originally_available_at | ?                        | ?                         |
TV_Show - Episode - rating                  | ?                        | ?                         |
TV_Show - Episode - absolute_index          | ?                        | ?                         |
TV_Show - Episode - writers                 | ?                        | ?                         |
TV_Show - Episode - directors               | ?                        | ?                         |
TV_Show - Episode - producers               | ?                        | ?                         |
TV_Show - Episode - thumbs                  | ?                        | ?                         |
----------------------------------------------------------------------------------------------------
```
