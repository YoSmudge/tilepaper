[![Build Status](https://travis-ci.org/samarudge/tilepaper.svg?branch=master)](https://travis-ci.org/samarudge/tilepaper)
[![codecov.io](https://codecov.io/github/samarudge/tilepaper/coverage.svg?branch=master)](https://codecov.io/github/samarudge/tilepaper?branch=master)

# tilepaper

## Generate a sort of tiled image thingy a bit like the Mac screensaver

### About

TL;DR use a folder of images to generate something like [this](http://cl.codes.am/dcrV)

On all my Mac's I have a folder of pictures, for the screensaver I used the tiled images option which generates a really nice scrolly thing with all the images on which I really like, but my desktop background is just a rotation of those same images.

Now having the images full size as my wallpaper is fine, but I'd much rather see multiple images in the same screen, so I threw together this quick project to generate those

### Usage

First install (probably in a virtualenv), with `pip install titlepaper`

Then run the tilepaper command

    tilepaper --source=./example-images/ --destination=./test-output --config=./example-config.yml --verbose

Compatible with Python 2.7+ and Python 3. Requires PIL, PyYAML and LibMagic

### Tests

You can test the whole render process with

    nosetests -v tests/testTiler.py:testTiler.test_fullProcess

Or run the individual unit tests with

    nosetests -v --exclude=test_fullProcess --with-coverage --cover-package=tilepaper

### Known issues

 * Sometimes tiles have black spaces on them, because my grid algorithm is terrible - _FIXED_ 0.1.4
 * Black line at right edge of some images (Rounding down bug?)

### Unknown issues

Multiple
