#!/usr/bin/env python
"""Handy utilities."""

import sys

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


def color_output(txt):
    """Color system writes."""
    colored = highlight(str(txt), PythonLexer(), TerminalFormatter())
    sys.stdout.write(colored + '\n')

