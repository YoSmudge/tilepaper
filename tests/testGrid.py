import tilepaper.grid
from nose.tools import ok_, eq_
import testBase


class testGrid(testBase.testBase):
    """
    Test grid generation
    """

    def test_sizing(self):
        """
        Returns correctly sized images
        """

        for im in self.testImages:
            sizings = []
            imC = self.imageClass(im)
            g = self.gridClass

            for i in range(0, 1000):
                sizings.append(g.getImageSize(imC))

            # Expect ~20% of images to be 2x2 if not portrait
            largeImages = len(
                [True for s in sizings if s[0] == 2 and s[1] == 2]
            )

            if imC.portrait:
                ok_(largeImages == 0)
            else:
                print("Large images: %d" % largeImages)
                ok_(largeImages > 150)
                ok_(largeImages < 350)

    def test_imagePosition(self):
        """
        Returns a valid position for an image
        """

        g = self.gridClass
        g.grid = self.fakeGrid
        g.getImageSize = lambda i, s: (1, 1)

        freePos = g.grid[5]
        del g.grid[5]

        print(freePos)
        p = g.getImagePosition(self.imageClass())
        eq_(p[0], freePos['x'])
        eq_(p[1], freePos['y'])

    def test_largeImage(self):
        """
        Positions a large image correctly
        """

        g = self.gridClass
        g.grid = self.fakeGrid

        deleteIndexes = [
            i for i in g.grid
            if i['x'] in [0, 1] and i['y'] in [0, 1]
        ]
        for d in deleteIndexes:
            del g.grid[g.grid.index(d)]

        g.getImageSize = lambda i, s: (2, 2)
        p = g.getImagePosition(self.imageClass())
        eq_(p[0], 0)
        eq_(p[1], 0)
        eq_(p[2], 2)
        eq_(p[3], 2)

    def test_breakNoSpace(self):
        """
        Fills grid once and only once
        """

        images = []
        for i in range(0, 500):
            images.append(self.imageClass())

        g = tilepaper.grid.Grid(
            images,
            (5, 5)
        )

        eq_(g.full, True)
        for x in range(0, 5):
            for y in range(0, 5):
                ocPs = len([
                    i for i in g.occupiedCoords
                    if i[0] == x and i[1] == y
                ])
                eq_(ocPs, 1)

    def test_noSpace(self):
        """
        No space left on grid
        """

        g = self.gridClass
        g.grid = self.fakeGrid
        p = g.getImagePosition(self.imageClass())
        eq_(p, None)

    def test_full(self):
        """
        Detection of a full grid
        """

        g = self.gridClass
        g.grid = self.fakeGrid
        eq_(g.full, True)
        del g.grid[5]
        eq_(g.full, False)

    def test_gridCoords(self):
        """
        Returns correct coordinates for grid
        """

        g = self.gridClass
        g.grid = self.fakeGrid

        eq_(len(g.grid), 25)
        eq_(all([c for c in g.gridCoords if c[0] <= 5 and c[1] <= 5]), True)
