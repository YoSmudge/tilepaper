import random


class Grid(object):
    """
    Grid object (Single tile)
    """

    pickedImages = []
    grid = []

    def __init__(self, images, gridSize):
        self.images = images
        random.shuffle(self.images)
        self.gridSize = gridSize
        self.grid = []

        for im in self.images:
            pos = self.getImagePosition(im)
            if not pos:
                pos = self.getImagePosition(im, small=True)
                if not pos:
                    break

            self.grid.append({
                "x": pos[0],
                "y": pos[1],
                "width": pos[2],
                "height": pos[3],
                "image": im
            })

    def getImageSize(self, im, small=False):
        if im.portrait:
            height = 2
            width = 1
        else:
            if random.randint(0, 10) <= 2 and not small:
                height = 2
                width = 2
            else:
                height = 1
                width = 1

        return width, height

    def getImagePosition(self, im, small=False):
        """
        Calculate the position by checking against the status of the grid
        """
        width, height = self.getImageSize(im, small)
        for x, y in self.gridCoords:
            # Check coords are within grid
            if not all(
                [x+xPos <= self.gridSize[0] for xPos in range(0, width+1)]
            ) or not all(
                [y+yPos <= self.gridSize[1] for yPos in range(0, height+1)]
            ):
                continue

            if any(i in self.occupiedCoords
                   for i in self.imageGridCoords(x, y, width, height)):
                continue

            return x, y, width, height

    def imageGridCoords(self, xBase, yBase, width, height):
        """
        Return a list of positions occupied by an image
        """
        coords = []
        for xPos in range(0, width):
            for yPos in range(0, height):
                coords.append([
                    xPos+xBase,
                    yPos+yBase
                ])
        return coords

    @property
    def full(self):
        """
        Does the grid have any free space on it
        """

        return all(c in self.occupiedCoords for c in self.gridCoords)

    @property
    def occupiedCoords(self):
        """
        Return all coords with an image in
        """

        coords = []
        for im in self.grid:
            for x, y in self.imageGridCoords(
                im['x'],
                im['y'],
                im['width'],
                im['height']
            ):
                coords.append([x, y])
        return coords

    @property
    def gridCoords(self):
        """
        Return a list of all possible grid coords
        """
        coords = []
        for x in range(0, self.gridSize[0]):
            for y in range(0, self.gridSize[1]):
                coords.append([x, y])
        return coords
