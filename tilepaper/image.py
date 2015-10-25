from PIL import Image as Img
from PIL import ImageOps


class Image(object):
    """
    Image object
    """

    def __init__(self, filePath):
        self.file = filePath
        _f = self.rawFile
        self.im = Img.open(_f)
        self.size = self.im.size
        _f.close()

    def resize(self, width, height):
        """
        Resize the image to the specified size
        Resizes with croping/scaling
        """
        with self as im:
            return ImageOps.fit(im, (width, height), centering=(0.5, 0.5))

    def ratioChange(self, rFrom, rTo):
        return float(rTo) / float(rFrom)

    def __enter__(self):
        self._file = self.rawFile
        return Img.open(self._file)

    def __exit__(self, *sp):
        self._file.close()

    @property
    def rawFile(self):
        return open(self.file, 'rb')

    @property
    def aspect(self):
        return float(self.im.size[0]) / float(self.im.size[1])

    @property
    def portrait(self):
        return self.aspect < 1
