from nose.tools import eq_
import PIL
import os
import shutil
import testBase


class TestImage(testBase.testBase):
    """
    Test image loading and resizing
    """

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
        for example in [
                       [100, 50], [256, 256], [50, 100], [512, 512],
                       [500, 512], [400, 512], [300, 512], [200, 512],
                       [512, 500], [512, 400], [512, 300], [512, 200]
        ]:
            for im in self.testImages:
                i = self.imageClass(im)
                r = i.resize(*example)
                eq_(r.size[0], example[0])
                eq_(r.size[1], example[1])
