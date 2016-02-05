#!/usr/bin/env python
"""Minimal linear algebra operations to matrices."""

import ast
import numpy as np

input_vars = {}


def save_namespace(filename='.workspace.mat'):
    """Save the current workspace."""
    namespace_file = open(filename, 'wb')
    namespace_file.write(str(input_vars) + '\n')
    namespace_file.close()


def load_namespace(filename='.workspace.mat'):
    """Load saved workspace if any."""
    try:
        namespace_file = open(filename, 'r')
        v = namespace_file.read()
        namespace_file.close()

        vars = ast.literal_eval(v)
        input_vars.update(vars)
    except IOError:
        pass


class Matrix(object):  # noqa

    """Perform basic matrix operations."""

    def __init__(self):
        """Initialize the matrix class.

        :token: list or string to matrix.
        """
        pass

    def to_matrix(self, tokens):
        """Transform list or string to matrix."""
        tokens = str(tokens)
        try:
            if tokens.find(';') < 0:
                return np.array(tokens)
            else:
                tokens.replace('[', '')
                tokens.replace(']', '')
                return np.matrix(tokens)
        except ValueError:
            return None

    def var_assigner(self, var_dict):
        """Keep track of assigned variables."""
        input_vars[str(var_dict[0])] = str(var_dict[1])

    def find_variable(self, var):
        """Find the variable value or raise error."""
        value = input_vars.get(str(var), None)
        return value

    def transpose(self, mx):
        """Perform a transpose."""
        return np.transpose(mx)

    def arith(self, operands):
        """Perform arithmetic operations."""
        try:
            result = ''
            if operands[2] == '+':
                result = operands[0] + operands[1]
            elif operands[2] == '-':
                result = operands[0] - operands[1]
            elif operands[2] == '*':
                result = np.dot(operands[0], operands[1])
            elif operands[0].startswith('inv'):
                result = np.linalg.inv(operands[1])
            return result
        except (TypeError, ValueError, np.linalg.LinAlgError):
            return None

