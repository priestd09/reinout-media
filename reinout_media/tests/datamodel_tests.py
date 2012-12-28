import unittest

from reinout_media import datamodels


class TestPhoto(unittest.TestCase):

    def test_smoke(self):
        photo = datamodels.Photo()
        self.assertTrue(photo)
