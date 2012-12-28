import os
import pkg_resources
import unittest

from reinout_media import datamodels


SAMPLE_CHRISTMAS_CARD = 'kerstkaart_annie_reinout_2012.jpg'

class TestPhoto(unittest.TestCase):

    def setUp(self):
        self.basepath = pkg_resources.resource_filename(
            'reinout_media.tests', 'testphotos')
        self.sample_photo_path = os.path.join(self.basepath,
                                              SAMPLE_CHRISTMAS_CARD)

    def test_smoke(self):
        photo = datamodels.Photo()
        self.assertTrue(photo)

    def test_init(self):
        photo = datamodels.Photo(self.sample_photo_path)
        self.assertEquals(photo.path, self.sample_photo_path)

    def test_relative_path(self):
        photo = datamodels.Photo('/a/b/c.jpg', basepath='/a')
        self.assertEquals(photo.relative_path, 'b/c.jpg')

    def test_relative_path2(self):
        # With no basepath set, return full path.
        photo = datamodels.Photo('/a/b/c.jpg')
        self.assertEquals(photo.relative_path, '/a/b/c.jpg')

    def test_name_from_filename(self):
        photo = datamodels.Photo(self.sample_photo_path)
        self.assertEquals(photo.name_from_filename,
                          'Kerstkaart annie reinout 2012')

    def test_name_with_only_filename(self):
        # Without an explicit name, use the filename as name.
        photo = datamodels.Photo(self.sample_photo_path)
        self.assertEquals(photo.name,
                          'Kerstkaart annie reinout 2012')


class TestTree(unittest.TestCase):

    def setUp(self):
        self.basepath = pkg_resources.resource_filename(
            'reinout_media.tests', 'testphotos')

    def test_smoke(self):
        tree = datamodels.Tree()
        self.assertTrue(tree)

    def test_init(self):
        tree = datamodels.Tree(self.basepath)
        self.assertEquals(tree.path, self.basepath)

    def test_photo_loading(self):
        tree = datamodels.Tree(self.basepath)
        self.assertTrue(tree.photos[0].path.endswith(
                SAMPLE_CHRISTMAS_CARD))

    def test_relative_paths_available(self):
        tree = datamodels.Tree(self.basepath)
        photo = tree.photos[0]
        self.assertEquals(photo.relative_path, SAMPLE_CHRISTMAS_CARD)
