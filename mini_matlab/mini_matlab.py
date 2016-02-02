#!/usr/bin/env python
"""Main Entry point for Mini Matlab."""

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

from tokenizer import Tokenizer

__version__ = "0.0.1"
__author__ = "Herbert Kagumba"
__license__ = "MIT"


def main(prompt='Mini Matlab >> '):
    """A prompt-read-eval loop."""
    while True:
        val = raw_input(prompt)
        if val == 'exit':
            break
        the_tokens = Tokenizer(val)
        tokens = the_tokens.lexer()
        print highlight(str(tokens), PythonLexer(), TerminalFormatter())


if __name__ == '__main__':
    main()
