import os
import logging


logger = logging.getLogger(__name__)


class Photo(object):
    """Wrapper around actual filesystem photo.

    A Photo object is dynamically generated based on an actual photo file. It
    can receive additional metadata. Probably it can extract metadata from the
    photo file.

    It should be able to provide any information another part of the system
    might need about a photo.

    """

    def __init__(self, path=None):
        self.path = path

    @property
    def name_from_filename(self):
        filename, ext = os.path.splitext(os.path.basename(self.path))
        return filename.replace('_', ' ').capitalize()

    @property
    def name(self):
        return self.name_from_filename  # For now this is enough.


class Tree(object):
    """Wrapper around a directory structure.

    A Tree object wraps a directory. It can read the whole directory
    (including subdirectories (note: not yet)) and detects (for now) photo
    files. It returns the detected photo files as (for now) a simple list of
    :class:`Photo` objects. Later on there'll be a tree structure, probably.

    Also later: detect a metadata ``.json`` file and set that all up.

    """

    def __init__(self, path=None):
        self.path = path
        if self.path is not None:
            self.photos = list(self._collect_photos())

    def _collect_photos(self):
        """Return all photo files in the directory.

        For now, just return with Photo objects with os.listdir. Use os.walk
        later on, including jpg/mov/flv detection.

        """
        for filename in os.listdir(self.path):
            # if not filename.endswith('.jpg'):
            #     continue
            full_filename = os.path.join(self.path, filename)
            yield Photo(full_filename)
