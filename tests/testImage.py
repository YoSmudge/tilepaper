import tilepaper.image
from nose.tools import *
import PIL
import os
import shutil


class TestImage(object):
    """
    Test image loading and resizing
    """

    def imageClass(self, imFile='140101-145456-00014-3433.jpg'):
        return tilepaper.image.Image(os.path.join('example-images', imFile))

    def testOpen(self):
        """
        Opens an image and provides the image object
        """

        i = self.imageClass()
        eq_(type(i.im), PIL.JpegImagePlugin.JpegImageFile)
        eq_(i.size[0], 750)
        eq_(i.size[1], 500)

    def testRatioChange(self):
        """
        Ratio change calculation is correct
        """

        eq_(self.imageClass().ratioChange(100, 50), 0.5)
        eq_(self.imageClass().ratioChange(50, 100), 2)

    def testAspectRatio(self):
        """
        Returns the correct aspect ratio
        """

        eq_(self.imageClass().aspect, 1.5)

    def testPortrait(self):
        """
        Detects portrait images
        """

        eq_(self.imageClass().portrait, False)
        eq_(self.imageClass('140101-145005-00012-3423.jpg').portrait, True)

    def testResize(self):
        """
        Returns a correctly resized image
        """

        if os.path.isdir('test-resizes'):
            shutil.rmtree('test-resizes')
        os.mkdir('test-resizes')
        for example in [[100, 50], [256, 256], [50, 100]]:
            for im in [
                       '140101-145005-00012-3423.jpg',
                       '140101-145456-00014-3433.jpg'
                       ]:
                i = self.imageClass(im)
                r = i.resize(*example)
                eq_(r.size[0], example[0])
                eq_(r.size[1], example[1])
                r.save(os.path.join(
                    'test-resizes',
                    '%s-%dx%d.jpg'
                    % (im, example[0], example[1])
                ))
