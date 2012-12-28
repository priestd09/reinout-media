import os


class Photo(object):
    """Wrapper around actual filesystem photo.

    A Photo object is dynamically generated based on an actual photo file. We
    can receive additional metadata. Probably we can extract metadata from the
    photo file.

    We should be able to provide any information another part of the system
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
