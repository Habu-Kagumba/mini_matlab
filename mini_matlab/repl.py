#!/usr/bin/env python
"""REPL functionalities."""

from __future__ import unicode_literals
from prompt_toolkit import prompt
from pygments.lexers import MathematicaLexer
from prompt_toolkit.history import FileHistory
from prompt_toolkit.contrib.completers import WordCompleter

import sys
import os

from parser import Parser


intro = """ Welcome to Mini Matlab, a minimal Matlab clone.
-----------------------------------------------

Commands:
    Exit - `exit`
    Help = `help`"""

help = """ """


class MatlabFileHistory(FileHistory):  # noqa

    """Override FileHistory functionality."""

    def __init__(self, filename):
        """Initialize the MatlabFileHistory class.

        Super the parent class.
        """
        self.filename = filename
        super(MatlabFileHistory, self).__init__(self.filename)

    def append(self, string):
        """Override the append function.

        Eliminate the date written in the files.
        Instead create a dictionary with the saved objects.
        """
        self.strings.append(string)

        with open(self.filename, 'ab') as f:
            def write(t):
                f.write(t.encode('utf-8'))
            for line in string.split('\n'):
                write('+{}\n'.format(line))


class Repl(object):  # noqa

    """Mini Matlab REPL."""

    def __init__(self, filename):
        """Initialize the REPL.

        :filename: History file.
        """
        self.filename = filename
        self.hist = MatlabFileHistory(self.filename)

    def autocomplete(self):
        """Setup autocompletion."""
        if os.path.isfile(self.filename):
            file = open(self.filename)
            hist_list = file.read()
            autocomplete_list_interim = hist_list.split('\n')
            autocomplete_list = [
                i.replace('+', '') for i in autocomplete_list_interim]

            return WordCompleter(
                list(set(autocomplete_list)), ignore_case=True)

    def run_repl(self):
        """Run the REPL loop."""
        sys.stdout.write(str(intro) + '\n')
        while True:
            try:
                val = prompt(
                    'Mini Matlab >> ',
                    lexer=MathematicaLexer,
                    history=self.hist,
                    completer=self.autocomplete()
                )
                if val == 'exit':
                    break
                elif val == 'help':
                    sys.stdout.write(str(intro) + '\n')
                else:
                    parser = Parser(val)
                    parser.save_retrieve_args()
            except (KeyboardInterrupt, SystemExit, EOFError):
                sys.stdout.write('Goodbye!!!\n')
                sys.exit(1)

