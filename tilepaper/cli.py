from argparse import ArgumentParser
import logging
import tilepaper.tiler
import tilepaper.config


def run():
    p = ArgumentParser()
    p.add_argument('--source', required=True)
    p.add_argument('--destination', required=True)
    p.add_argument('--config', required=True)
    p.add_argument('--quiet', action="store_true")
    p.add_argument('--verbose', action="store_true")
    options = p.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif options.quiet:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.INFO)

    config = tilepaper.config.load(options.config)
    t = tilepaper.tiler.generator()
    t.process(
        source=options.source,
        dest=options.destination,
        **config
    )


if __name__ == "__main__":
    run()
