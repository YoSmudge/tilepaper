import tilepaper.image
import os
import shutil


class testBase(object):
    """
    Base helpers for tests
    """

    testImages = [
        '140101-145005-00012-3423.jpg',
        '140101-145456-00014-3433.jpg'
    ]

    def setUp(self):
        if os.path.isdir('test-resizes'):
            shutil.rmtree('test-resizes')
        os.mkdir('test-resizes')

        if os.path.isdir('test-output'):
            shutil.rmtree('test-output')
        os.mkdir('test-output')

    def tearDown(self):
        if os.path.isdir('example-images/subdir'):
            shutil.rmtree('example-images/subdir')

    def imageClass(self, imFile='140101-145456-00014-3433.jpg'):
        return tilepaper.image.Image(os.path.join('example-images', imFile))

    @property
    def imageList(self):
        return [self.imageClass(i) for i in self.testImages]

    @property
    def gridClass(self):
        """
        Basic grid class
        """

        return tilepaper.grid.Grid(
            self.imageList,
            (5, 5)
        )

    @property
    def fakeGrid(self):
        """
        Return a fake image grid list
        """
        # Fill grid with fake images
        fakeGrid = []
        for x in range(0, 5):
            for y in range(0, 5):
                fakeGrid.append({
                    'x': x,
                    'y': y,
                    'width': 1,
                    'height': 1,
                    'image': self.imageClass()
                })
        return fakeGrid
