# tilepaper

## Generate a sort of tiled image thingy a bit like the Mac screensaver

### About

TL;DR use a folder of images to generate something like [this](http://cl.codes.am/dcrV)

On all my Mac's I have a folder of pictures, for the screensaver I used the tiled images option which generates a really nice scrolly thing with all the images on which I really like, but my desktop background is just a rotation of those same images.

Now having the images full size as my wallpaper is fine, but I'd much rather see multiple images in the same screen, so I threw together this quick project to generate those

### Usage

First install (probably in a virtualenv), with `python setup.py install`

Then run the tilepaper command

    tilepaper --source=./example-images/ --destination=./test-output --config=./example-config.yml --verbose

Developed against Python 3.4, YMMV with other versions. Requires PIL, PyYAML and LibMagic

### Tests

Run it, see if it works - I might do real tests some time

### Known issues

Sometimes tiles have black spaces on them, because my grid algorithm is terrible

### Unknown issues

Multiple
