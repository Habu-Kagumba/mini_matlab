#!/usr/bin/env python
"""Main Entry point for Mini Matlab."""

import sys

__version__ = "0.0.1"
__author__ = "Herbert Kagumba"
__license__ = "MIT"


def main(prompt='Mini Matlab >> '):
    """Main entry for the application."""
    while True:
        val = raw_input(prompt)
        sys.stderr.write('You entered: %s\n' % val)
        sys.exit(1)


if __name__ == '__main__':
    main()
