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

        :chars: Passed in arguments to parse from the the repl.
        """
        self.chars = chars

        bounds = 'BOUNDS'
        operator = 'OPERATOR'
        variable = 'VARIABLE'
        assignment = 'ASSIGNMENT'
        ints = 'INTS'

        # the expression used to parse and group the arguments
        expressions = [
            (r'[ \n\t ]+', None),
            (r'#[^\n]*', None),
            (r'inv\([a-zA-Z]\)', operator),
            (r'[a-zA-Z]', variable),
            (r'\=', assignment),
            (r'\[([0-9, ;]+)\]', bounds),
            (r'\d', ints),
            (r'\+', operator),
            (r'-', operator),
            (r'\*', operator),
            (r'\'', operator)
        ]

        self.exprs = expressions

    @staticmethod
    def tokenizer(arguments, patterns_exprs):
        """Parse the arguments against the expressions.

        :arguments: The arguments to be parsed.
        :patterns_exprs: the pattern expression for matching.
        """
        pos = 0
        tokens = []
        while pos < len(arguments):
            match = None
            for expr in patterns_exprs:
                pattern, tag = expr
                regex = re.compile(pattern)
                match = regex.match(arguments, pos)
                if match:
                    text = match.group(0)
                    if tag:
                        token = (tag, text)
                        tokens.append(token)
                    break
            if not match:
                sys.stdout.write(
                    'Illegal character: `%s`\n' % arguments[pos])
                break
            else:
                pos = match.end(0)
        return tokens

    def lexer(self):
        """Re-format the tokens for arithmetic operations."""
        tokens = self.tokenizer(self.chars, self.exprs)
        return tokens

