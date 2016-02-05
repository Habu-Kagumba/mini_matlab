#!/usr/bin/env python
"""Parse the input."""

import re

from tokenizer import Tokenizer
from matrix import Matrix
from utils import color_output


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
        self.ints = 'INTS'

    def retrieve_args(self, tokens):
        """Format the tokens and save them to file."""
        m = Matrix()
        if len(tokens) == 1:
            # variable call or display array / matrix
            if tokens[0][0] == self.variable:
                # variable call
                value = m.find_variable(tokens[0][1])
                if value:
                    value_mx = m.to_matrix(value)
                    if value_mx is not None:
                        color_output(value_mx)
                    else:
                        color_output('Input error.')
                else:
                    color_output(
                        'Variable `{}` not defined.'.format(
                            str(tokens[0][1])))
            elif tokens[0][0] == self.bounds:
                # display array / list
                mx = m.to_matrix(tokens[0][1])
                if mx is not None:
                    color_output(mx)
                else:
                    color_output('Input error')
            elif tokens[0][0] == self.operator:
                o = tokens[0][1]
                if o.startswith('inv'):
                    r = re.compile('\(\w\)')
                    p = r.search(o).group()
                    v = re.compile('\w')
                    var = v.search(p).group()
                    val = m.find_variable(var)
                    if val is not None:
                        var_x = m.to_matrix(val)
                        if var_x is not None:
                            res = m.arith(('inverse', var_x, None))
                            if res is not None:
                                color_output(res)
                            else:
                                color_output('Wrong matrix format.')
                        else:
                            color_output('Input error.')
                    else:
                        color_output(
                            'Variable `{}` not defined.'.format(
                                str(tokens[0][1])))
            else:
                color_output('Wrong input...')

        if len(tokens) == 2:
            if tokens[0][0] == self.variable:
                if tokens[1][0] != self.operator:
                    color_output('Wrong input...')
                else:
                    if tokens[1][1] == '\'':
                        tr_value = m.find_variable(tokens[0][1])
                        if tr_value:
                            tr_value_mx = m.to_matrix(tr_value)
                            if tr_value_mx is not None:
                                tr = m.transpose(tr_value_mx)
                                color_output(str(tr))
                            else:
                                color_output('Input error.')
                        else:
                            color_output(
                                'Variable `{}` not defined.'.format(
                                    str(tokens[0][1])))
                    else:
                        color_output('Wrong input...')
            else:
                color_output('Wrong input...')

        if len(tokens) == 3:
            if tokens[0][0] == self.variable:
                if tokens[1][0] == self.assignment:
                    if tokens[2][0] == self.bounds:
                        input_var = tokens[0][1]
                        assign = tokens[2][1]
                        save_vars = (input_var, assign)
                        m.var_assigner(save_vars)
                    elif tokens[2][0] == self.variable:
                        assigner = tokens[0][1]
                        assignee = tokens[2][1]
                        assigner_val = m.find_variable(assigner)
                        if assigner_val:
                            m.var_assigner((assignee, assigner_val))
                        else:
                            color_output(
                                'Variable `{}` not defined.'.format(
                                    str(assigner)))
                elif tokens[1][0] == self.operator:
                    op = tokens[1][1]
                    op_var = m.find_variable(tokens[0][1])
                    if op_var is not None:
                        op_vars = m.to_matrix(op_var)
                        if tokens[2][0] == self.bounds:
                            op_bounds = m.to_matrix(tokens[2][1])
                            if op_bounds is not None:
                                op_res = m.arith((op_vars, op_bounds, op))
                                print op_res
                                if op_res is not None:
                                    color_output(str(op_res))
                                else:
                                    color_output(
                                        'Operation not valid.')
                            else:
                                color_output('Input error.')
                        elif tokens[2][0] == self.variable:
                            val = m.find_variable(tokens[2][1])
                            if val is not None:
                                var_value = m.to_matrix(val)
                                op_results = m.arith(
                                    (op_vars, var_value, op))
                                if op_results is not None:
                                    color_output(str(op_results))
                                else:
                                    color_output(
                                        'Operation not valid.')
                            else:
                                color_output(
                                    'Variable `{}` not defined.'.format(
                                        tokens[2][1]))
                    else:
                        color_output(
                            'Variable `{}` not defined.'.format(
                                tokens[0][1]))
                else:
                    color_output('Wrong input...')
            elif tokens[0][0] == self.bounds:
                if tokens[1][0] == self.operator:
                    if tokens[2][0] == self.self.bounds:
                        color_output('Perform operation on bounds.')
                    elif tokens[2][0] == self.variable:
                        color_output('Perform operation on variable.')
                else:
                    color_output('Wrong input...')

        if len(tokens) > 3:
            color_output('Not implemented yet. WIP')

    def save_retrieve_args(self):
        """Save and retrieve arguments."""
        the_tokens = Tokenizer(self.vals)
        tokens = the_tokens.lexer()
        self.retrieve_args(tokens)

