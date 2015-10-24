from PIL import Image as Img


class TileRenderer(object):
    def __init__(self, grid, tileSize, cellSize, border, filePath):
        self.tileSize = tileSize
        self.cellSize = cellSize
        self.im = Img.new("RGB", tileSize)
        self.filePath = filePath

        for i, tile in enumerate(grid.grid):
            sizeX = (cellSize[0]*tile['width'] - border['size'])
            sizeY = (cellSize[1]*tile['height'] - border['size'])

            r = tile['image'].resize(sizeX, sizeY)
            box = (
                int(cellSize[0]*tile['x']+border['size']/2),
                int(cellSize[1]*tile['y']+border['size']/2)
            )
            self.im.paste(r, box)

        self.im.save(filePath, 'JPEG')
