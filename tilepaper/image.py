from PIL import Image as Img

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

    def resize(self,width,height):
        """
        Resize the image to the specified size
        Resizes with croping/scaling
        """
        with self as im:
            xofs, yofs = 0, 0
            wRatio = self.ratioChange(self.size[0], width)
            hRatio = self.ratioChange(self.size[1], height)
            cHeight = int(self.size[1]*wRatio)
            cWidth = int(self.size[0]*hRatio)
            if cWidth > width:
                xofs = (cWidth-width)/wRatio/2
            else:
                yofs = (cHeight-height)/hRatio/2

            cropBox = [int(p) for p in [xofs, yofs, self.size[0]-xofs, self.size[1]-yofs]]
            rsz = im.crop(cropBox)
            return rsz.resize((width,height), Img.ANTIALIAS)


    def ratioChange(self,rFrom,rTo):
        return float(rTo) / float(rFrom)

    def __enter__(self):
        self._file = self.rawFile
        return Img.open(self._file)

    def __exit__(self,*sp):
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
