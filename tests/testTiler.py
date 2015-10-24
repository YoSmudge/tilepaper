from nose.tools import *
import tilepaper.tiler
import tilepaper.config
import os
import shutil
from PIL import Image as Img
import magic


class testTiler(object):
    """
    Test the full tiler process
    """

    def test_findImages(self):
        """
        Finding images in source directory
        """

        t = tilepaper.tiler.generator()
        images = t.findImages('example-images')
        eq_(len(images), 37)

    def test_skipFiles(self):
        """
        Finding images only returns images
        """

        txtFile = os.path.join('example-images', 'testfile.txt')
        open(txtFile, 'w').close()
        t = tilepaper.tiler.generator()
        images = t.findImages('example-images')
        eq_(len(images), 37)
        ok_(not any(
            [i for i in images if os.path.basename(i.file) == 'testfile.txt']
        ))
        os.remove(txtFile)

    def test_fullProcess(self):
        """
        Full render process
        """

        if os.path.isdir('test-output'):
            shutil.rmtree('test-output')
        os.mkdir('test-output')
        t = tilepaper.tiler.generator()
        c = tilepaper.config.load('./example-config.yml')
        t.process('example-images', 'test-output', **c)

        testFile = 'test-output/1366x768/000001.jpg'
        assert_true(os.path.isfile(testFile))
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
            eq_(m.id_filename(testFile), 'image/jpeg')

        with open(testFile, 'rb') as f:
            i = Img.open(f)
        eq_(i.size[0], 1366)
        eq_(i.size[1], 768)
