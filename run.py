"""
Script entry point
"""
import logging

from tablify.cli import app

LOGLEVEL = 'INFO'


def main():
    logging.basicConfig(
        format='%(message)s',
        level=getattr(logging, LOGLEVEL)
    )
    logging.debug('Initializing')
    app()


if __name__ == '__main__':
    main()