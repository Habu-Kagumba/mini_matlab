#!/usr/bin/env python
"""Parse the input."""

import sys

from tokenizer import Tokenizer


class Parser(object):  # noqa

    """Input parser: parse token arguments."""

    def __init__(self, vals):
        """Initialize Parser.

        :tokens: lexed argument inputs.
        """
        self.vals = vals
        self.bounds = 'BOUNDS'
        self.operator = 'OPERATOR'
        self.variable = 'VARIABLE'
        self.assignment = 'ASSIGNMENT'

    def retrieve_args(self, tokens):
        """Format the tokens and save them to file."""
        if len(tokens) == 1:
            # variable call or display array / matrix
            if tokens[0][0] == self.variable:
                # variable call
                sys.stdout.write('Calling a varibale.\n')
            elif tokens[0][0] == self.bounds:
                # display array / list
                sys.stdout.write('Display array or list\n')
            else:
                sys.stdout.write('Wrong input...\n')

        if len(tokens) == 2:
            if tokens[0][0] == self.variable:
                if tokens[1][0] != self.operator:
                    sys.stdout.write('Wrong input...\n')
                else:
                    if tokens[1][1] == '\'':
                        sys.stdout.write('Perform a transpose.\n')
                    else:
                        sys.stdout.write('Wrong input...\n')

        if len(tokens) == 3:
            if tokens[0][0] == self.variable:
                if tokens[1][0] == self.assignment:
                    if tokens[2][0] == self.bounds:
                        sys.stdout.write('Variable assignment.\n')
                    elif tokens[2][0] == self.variable:
                        sys.stdout.write('Re-assign variables.\n')
                elif tokens[1][0] == self.operator:
                    if tokens[2][0] == self.bounds:
                        sys.stdout.write('Perform an operation on bounds.\n')
                    elif tokens[2][0] == self.variable:
                        sys.stdout.write(
                            'Perform an operation on variable.\n')
                else:
                    sys.stdout.write('Wrong input...\n')
            elif tokens[0][0] == self.bounds:
                if tokens[1][0] == self.operator:
                    if tokens[2][0] == self.self.bounds:
                        sys.stdout.write('Perform operation on bounds.\n')
                    elif tokens[2][0] == self.variable:
                        sys.stdout.write('Perform operation on variable.\n')
                else:
                    sys.stdout.write('Wrong input...\n')

        if len(tokens) > 3:
            sys.stdout.write('Not implemented yet. WIP\n')

    def save_retrieve_args(self):
        """Save and retrieve arguments."""
        the_tokens = Tokenizer(self.vals)
        tokens = the_tokens.lexer()
        self.retrieve_args(tokens)

