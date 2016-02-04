#!/usr/bin/env python
"""Main Entry point for Mini Matlab."""

from repl import Repl

__version__ = "0.0.1"
__author__ = "Herbert Kagumba"
__license__ = "MIT"


def main():
    """A prompt-read-eval loop."""
    repl = Repl('.save.mat')
    repl.run_repl()


if __name__ == '__main__':
    main()
