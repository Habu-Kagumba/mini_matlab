#!/usr/bin/env python
"""REPL arguments tokenizer."""

import sys
import re


class Tokenizer(object):  # noqa
    """Main class for the Tokenizer.

    Tokenize all the arguments passed into the REPL for parsing.
    """

    def __init__(self, chars):
        """Initialize the Tokenizer class.

        :chars: Passed in characters to parse from the the repl.
        """
        self.chars = chars

        bounds = 'BOUNDS'
        separator = 'SEPARATOR'
        operator = 'OPERATOR'
        int = 'INT'

        # the expression used to parse and group the arguments
        expressions = [
            (r'[ \n\t ]+', None),
            (r'#[^\n]*', None),
            (r'\[', bounds),
            (r'\]', bounds),
            (r'\;', separator),
            (r'\+', operator),
            (r'-', operator),
            (r'\*', operator),
            (r'\'', operator),
            (r'[0-9]+', int)
        ]

        self.exprs = expressions

    @staticmethod
    def tokenizer(arguments, patterns_exprs):
        """Parse the characters against the expressions.

        :arguments: The characters to be parsed.
        :patterns_exprs: the pattern expression for matching.
        """
        characters = re.sub(r'\s*,\s*', ' ', arguments)

        pos = 0
        tokens = []
        while pos < len(characters):
            match = None
            for expr in patterns_exprs:
                pattern, tag = expr
                regex = re.compile(pattern)
                match = regex.match(characters, pos)
                if match:
                    text = match.group(0)
                    if tag:
                        token = (text, tag)
                        tokens.append(token)
                    break
            if not match:
                sys.stderr.write('Illegal character: %s\n' % characters[pos])
                sys.exit(1)
            else:
                pos = match.end(0)
        return tokens

    def lexer(self):
        """Re-format the tokens for arithmetic operations."""
        tokens = self.tokenizer(self.chars, self.exprs)
        return tokens

