import tilepaper.renderer
from nose.tools import eq_
import testBase
import os
import magic


class testRenderer(testBase.testBase):

    def test_render(self):
        """
        Basic render
        """

        g = self.gridClass
        g.grid = self.fakeGrid
        tilepaper.renderer.TileRenderer(
            g,
            (100, 100),
            (500, 500),
            {'size': 1},
            'test-resizes/render.jpg'
        )

        eq_(os.path.isfile('test-resizes/render.jpg'), True)
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
            eq_(m.id_filename('test-resizes/render.jpg'), 'image/jpeg')
