from argparse import ArgumentParser
import sys
import logging
import snaptiler.tiler
import snaptiler.config

def run():
    p = ArgumentParser()
    p.add_argument('--source')
    p.add_argument('--destination')
    p.add_argument('--config')
    p.add_argument('--quiet', action="store_true")
    p.add_argument('--verbose', action="store_true")
    options = p.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif options.quiet:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.INFO)

    config = snaptiler.config.load(options.config)
    t = snaptiler.tiler.generator()
    t.process(
        source=options.source,
        dest=options.destination,
        **config
    )



if __name__ == "__main__":
    run()
