# -*- coding: utf-8 -*-
from urllib.parse import quote_plus

from plexapi import media, utils
from plexapi.base import Playable, PlexPartialObject
from plexapi.exceptions import BadRequest, NotFound


@utils.registerPlexObject
class Photoalbum(PlexPartialObject):
    """ Represents a photoalbum (collection of photos).

        Attributes:
            TAG (str): 'Directory'
            TYPE (str): 'photo'
            addedAt (datetime): Datetime this item was added to the library.
            art (str): Photo art (/library/metadata/<ratingkey>/art/<artid>)
            composite (str): Unknown
            fields (list): List of :class:`~plexapi.media.Field`.
            guid (str): Unknown (unique ID)
            index (sting): Index number of this album.
            key (str): API URL (/library/metadata/<ratingkey>).
            librarySectionID (int): :class:`~plexapi.library.LibrarySection` ID.
            listType (str): Hardcoded as 'photo' (useful for search filters).
            ratingKey (int): Unique key identifying this item.
            summary (str): Summary of the photoalbum.
            thumb (str): URL to thumbnail image.
            title (str): Photoalbum title. (Trip to Disney World)
            type (str): Unknown
            updatedAt (datatime): Datetime this item was updated.
    """
    TAG = 'Directory'
    TYPE = 'photo'

    def _loadData(self, data):
        """ Load attribute values from Plex XML response. """
        self.listType = 'photo'
        self.addedAt = utils.toDatetime(data.attrib.get('addedAt'))
        self.art = data.attrib.get('art')
        self.composite = data.attrib.get('composite')
        self.fields = self.findItems(data, etag='Field')
        self.guid = data.attrib.get('guid')
        self.index = utils.cast(int, data.attrib.get('index'))
        self.key = data.attrib.get('key')
        self.librarySectionID = data.attrib.get('librarySectionID')
        self.ratingKey = data.attrib.get('ratingKey')
        self.summary = data.attrib.get('summary')
        self.thumb = data.attrib.get('thumb')
        self.title = data.attrib.get('title')
        self.type = data.attrib.get('type')
        self.updatedAt = utils.toDatetime(data.attrib.get('updatedAt'))

    def albums(self, **kwargs):
        """ Returns a list of :class:`~plexapi.photo.Photoalbum` objects in this album. """
        key = '/library/metadata/%s/children' % self.ratingKey
        return self.fetchItems(key, etag='Directory', **kwargs)

    def album(self, title):
        """ Returns the :class:`~plexapi.photo.Photoalbum` that matches the specified title. """
        for album in self.albums():
            if album.title.lower() == title.lower():
                return album
        raise NotFound('Unable to find album: %s' % title)

    def photos(self, **kwargs):
        """ Returns a list of :class:`~plexapi.photo.Photo` objects in this album. """
        key = '/library/metadata/%s/children' % self.ratingKey
        return self.fetchItems(key, etag='Photo', **kwargs)

    def photo(self, title):
        """ Returns the :class:`~plexapi.photo.Photo` that matches the specified title. """
        for photo in self.photos():
            if photo.title.lower() == title.lower():
                return photo
        raise NotFound('Unable to find photo: %s' % title)

    def iterParts(self):
        """ Iterates over the parts of this media item. """
        for album in self.albums():
            for photo in album.photos():
                for part in photo.iterParts():
                    yield part

    def download(self, savepath=None, keep_original_name=False, showstatus=False):
        """ Download photo files to specified directory.

            Parameters:
                savepath (str): Defaults to current working dir.
                keep_original_name (bool): True to keep the original file name otherwise
                    a friendlier is generated.
                showstatus(bool): Display a progressbar.
        """
        filepaths = []
        locations = [i for i in self.iterParts() if i]
        for location in locations:
            name = location.file
            if not keep_original_name:
                title = self.title.replace(' ', '.')
                name = '%s.%s' % (title, location.container)
            url = self._server.url('%s?download=1' % location.key)
            filepath = utils.download(url, self._server._token, filename=name, showstatus=showstatus,
                                      savepath=savepath, session=self._server._session)
            if filepath:
                filepaths.append(filepath)
        return filepaths


@utils.registerPlexObject
class Photo(PlexPartialObject, Playable):
    """ Represents a single photo.

        Attributes:
            TAG (str): 'Photo'
            TYPE (str): 'photo'
            addedAt (datetime): Datetime this item was added to the library.
            fields (list): List of :class:`~plexapi.media.Field`.
            index (sting): Index number of this photo.
            key (str): API URL (/library/metadata/<ratingkey>).
            librarySectionID (int): :class:`~plexapi.library.LibrarySection` ID.
            listType (str): Hardcoded as 'photo' (useful for search filters).
            media (TYPE): Unknown
            originallyAvailableAt (datetime): Datetime this photo was added to Plex.
            parentKey (str): Photoalbum API URL.
            parentRatingKey (int): Unique key identifying the photoalbum.
            ratingKey (int): Unique key identifying this item.
            summary (str): Summary of the photo.
            thumb (str): URL to thumbnail image.
            title (str): Photo title.
            type (str): Unknown
            updatedAt (datatime): Datetime this item was updated.
            year (int): Year this photo was taken.
    """
    TAG = 'Photo'
    TYPE = 'photo'
    METADATA_TYPE = 'photo'

    def _loadData(self, data):
        """ Load attribute values from Plex XML response. """
        Playable._loadData(self, data)
        self.listType = 'photo'
        self.addedAt = utils.toDatetime(data.attrib.get('addedAt'))
        self.fields = self.findItems(data, etag='Field')
        self.index = utils.cast(int, data.attrib.get('index'))
        self.key = data.attrib.get('key')
        self.librarySectionID = data.attrib.get('librarySectionID')
        self.originallyAvailableAt = utils.toDatetime(
            data.attrib.get('originallyAvailableAt'), '%Y-%m-%d')
        self.parentKey = data.attrib.get('parentKey')
        self.parentRatingKey = data.attrib.get('parentRatingKey')
        self.ratingKey = data.attrib.get('ratingKey')
        self.summary = data.attrib.get('summary')
        self.thumb = data.attrib.get('thumb')
        self.title = data.attrib.get('title')
        self.type = data.attrib.get('type')
        self.updatedAt = utils.toDatetime(data.attrib.get('updatedAt'))
        self.year = utils.cast(int, data.attrib.get('year'))
        self.media = self.findItems(data, media.Media)
        self.tag = self.findItems(data, media.Tag)

    @property
    def thumbUrl(self):
        """Return URL for the thumbnail image."""
        key = self.firstAttr('thumb', 'parentThumb', 'granparentThumb')
        return self._server.url(key, includeToken=True) if key else None

    def photoalbum(self):
        """ Return this photo's :class:`~plexapi.photo.Photoalbum`. """
        return self.fetchItem(self.parentKey)

    def section(self):
        """ Returns the :class:`~plexapi.library.LibrarySection` this item belongs to. """
        if hasattr(self, 'librarySectionID'):
            return self._server.library.sectionByID(self.librarySectionID)
        elif self.parentKey:
            return self._server.library.sectionByID(self.photoalbum().librarySectionID)
        else:
            raise BadRequest('Unable to get section for photo, can`t find librarySectionID')

    def iterParts(self):
        """ Iterates over the parts of this media item. """
        for item in self.media:
            for part in item.parts:
                yield part

    def sync(self, resolution, client=None, clientId=None, limit=None, title=None):
        """ Add current photo as sync item for specified device.
            See :func:`plexapi.myplex.MyPlexAccount.sync()` for possible exceptions.

            Parameters:
                resolution (str): maximum allowed resolution for synchronized photos, see PHOTO_QUALITY_* values in the
                                  module :mod:`plexapi.sync`.
                client (:class:`plexapi.myplex.MyPlexDevice`): sync destination, see
                                                               :func:`plexapi.myplex.MyPlexAccount.sync`.
                clientId (str): sync destination, see :func:`plexapi.myplex.MyPlexAccount.sync`.
                limit (int): maximum count of items to sync, unlimited if `None`.
                title (str): descriptive title for the new :class:`plexapi.sync.SyncItem`, if empty the value would be
                             generated from metadata of current photo.

            Returns:
                :class:`plexapi.sync.SyncItem`: an instance of created syncItem.
        """

        from plexapi.sync import SyncItem, Policy, MediaSettings

        myplex = self._server.myPlexAccount()
        sync_item = SyncItem(self._server, None)
        sync_item.title = title if title else self.title
        sync_item.rootTitle = self.title
        sync_item.contentType = self.listType
        sync_item.metadataType = self.METADATA_TYPE
        sync_item.machineIdentifier = self._server.machineIdentifier

        section = self.section()

        sync_item.location = 'library://%s/item/%s' % (section.uuid, quote_plus(self.key))
        sync_item.policy = Policy.create(limit)
        sync_item.mediaSettings = MediaSettings.createPhoto(resolution)

        return myplex.sync(sync_item, client=client, clientId=clientId)

    def download(self, savepath=None, keep_original_name=False, showstatus=False):
        """ Download photo files to specified directory.

            Parameters:
                savepath (str): Defaults to current working dir.
                keep_original_name (bool): True to keep the original file name otherwise
                    a friendlier is generated.
                showstatus(bool): Display a progressbar.
        """
        filepaths = []
        locations = [i for i in self.iterParts() if i]
        for location in locations:
            name = location.file
            if not keep_original_name:
                title = self.title.replace(' ', '.')
                name = '%s.%s' % (title, location.container)
            url = self._server.url('%s?download=1' % location.key)
            filepath = utils.download(url, self._server._token, filename=name, showstatus=showstatus,
                                      savepath=savepath, session=self._server._session)
            if filepath:
                filepaths.append(filepath)
        return filepaths
