from nose.tools import eq_, ok_, assert_true, raises
import tilepaper.tiler
import tilepaper.config
import os
import shutil
from PIL import Image as Img
import magic
import testBase


class testTiler(testBase.testBase):
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

    def test_subdirs(self):
        """
        Include subdirectories
        """

        os.mkdir(os.path.join('example-images', 'subdir'))
        testImgDest = os.path.join(
            'example-images',
            'subdir',
            self.testImages[0]
        )
        shutil.copy(
            os.path.join('example-images', self.testImages[0]),
            testImgDest
        )

        t = tilepaper.tiler.generator()
        images = t.findImages('example-images')
        ok_(testImgDest in [i.file for i in images])

    def test_fullProcess(self):
        """
        Full render process
        """

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

    def test_tileGenerator(self):
        """
        Generating tiles
        """

        t = tilepaper.tiler.generator()
        images = t.findImages('example-images')
        tiles = t.generateTiles(
            images,
            (5, 5),
            10
        )

        ok_(len(tiles) > 0)
        ok_(type(tiles), list)

        # Check an image is used <= inclusions
        for i in images:
            tilesUsedIn = len([
                tl for tl in tiles
                if any(
                    c['image'].file for c in tl['grid'].grid
                    if c['image'].file == i.file
                )
            ])

            ok_(tilesUsedIn <= 10)

        # Check same image not used in tile more than once
        for t in tiles:
            for i in images:
                tileUsedTimes = len([
                    c for c in t['grid'].grid
                    if c['image'].file == i.file
                ])

                ok_(tileUsedTimes <= 1)

    def test_renderTiles(self):
        """
        Renders tiles to output
        """

        t = tilepaper.tiler.generator()
        images = t.findImages('example-images')
        tiles = t.generateTiles(
            images,
            (5, 5),
            10
        )

        t.dest = 'test-output'
        t.config = {
            'border': {
                'size': 1
            }
        }
        t.renderTiles(tiles, '500x500', [100, 100])

    @raises(tilepaper.tiler.ConfigException)
    def test_missingDirectories(self):
        """
        Raises exception when input or output dir doesn't exist
        """

        t = tilepaper.tiler.generator()
        t.process('not-found', 'not-found')
