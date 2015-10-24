import magic
import os
import logging
from tilepaper.image import Image
from tilepaper.grid import Grid
from tilepaper.renderer import TileRenderer


class ConfigException(Exception):
    None


class generator(object):
    imageTypes = ['image/jpeg', 'image/png']

    def process(self, source, dest, **config):
        self.source = os.path.abspath(
            os.path.expanduser(source)
        )
        self.dest = os.path.abspath(
            os.path.expanduser(dest)
        )
        self.config = config

        for d in [("Source", self.source), ("Destination", self.dest)]:
            if not os.path.isdir(d[1]):
                raise ConfigException("%s directory not found!" % d[0])

        images = self.findImages(self.source)
        logging.info("Found %d images" % len(images))

        for size in config['sizes']:
            logging.info("Generating tile format for %s" % size)
            gridSize = config['grid'][size]\
                if size in config['grid'] else config['grid']['default']
            tiles = self.generateTiles(
                images,
                gridSize,
                inclusions=config['inclusions']
            )
            logging.info("Generated %d tile layouts" % len(tiles))
            logging.info("Rendering")
            self.renderTiles(tiles, size, gridSize)

    def findImages(self, directory):
        """
        Recursive scan directory to find images
        """

        logging.debug("Finding images in %s" % directory)
        images = []
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
            for fileName in os.listdir(directory):
                fullPath = os.path.join(directory, fileName)

                if os.path.isdir(fullPath):
                    images += self.findImages(fullPath)
                else:
                    mimeType = m.id_filename(fullPath)
                    if mimeType in self.imageTypes:
                        images.append(Image(fullPath))
                    else:
                        logging.debug(
                            "Skipping file %s with mime %s"
                            % (fullPath, mimeType)
                        )
        return images

    def generateTiles(self, images, gridSize, inclusions):
        """
        Generate the tile formats
        """

        tileId = 1
        imageUses = {}
        tiles = []
        while True:
            avaliableImages = [
                im for im in images
                if im.file not in imageUses.keys() or
                imageUses[im.file] < inclusions
            ]

            if len(avaliableImages) == 0:
                break

            logging.debug(
                "Tile %06d with %d images remaining"
                % (tileId, len(avaliableImages))
            )
            grid = Grid(avaliableImages, gridSize)

            if grid.full:
                tiles.append({"id": tileId, "grid": grid})
                tileId += 1
            else:
                logging.debug("Tile not full, skipping")

            for cell in grid.grid:
                im = cell['image']
                if im.file not in imageUses:
                    imageUses[im.file] = 1
                else:
                    imageUses[im.file] += 1

        return tiles

    def renderTiles(self, tiles, size, gridSize):
        """
        Render out the tiles
        """

        tileSize = [int(c) for c in size.split('x')]
        cellSize = [
            int(float(tileSize[0])/float(gridSize[0])),
            int(float(tileSize[-1])/float(gridSize[-1]))
        ]

        renderDir = os.path.join(self.dest, size)
        if not os.path.isdir(renderDir):
            os.mkdir(renderDir)

        for tile in tiles:
            logging.debug("Rendering tile %d of %d" % (tile['id'], len(tiles)))
            filePath = os.path.join(
                renderDir,
                "%06d.jpg" % tile['id']
            )
            TileRenderer(tile['grid'],
                         tileSize,
                         cellSize,
                         self.config['border'],
                         filePath)
