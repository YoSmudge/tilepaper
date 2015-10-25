import tilepaper.image
import os


class testBase(object):
    """
    Base helpers for tests
    """

    testImages = [
        '140101-145005-00012-3423.jpg',
        '140101-145456-00014-3433.jpg'
    ]

    def imageClass(self, imFile='140101-145456-00014-3433.jpg'):
        return tilepaper.image.Image(os.path.join('example-images', imFile))

    @property
    def imageList(self):
        return [self.imageClass(i) for i in self.testImages]
