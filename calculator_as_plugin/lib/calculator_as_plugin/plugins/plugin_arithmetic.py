# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:23:02 2017

@author: a0229971
"""
from .plugin import Plugin as BasePlugin


class Plugin(BasePlugin):

    operations = ['sum', 'sub', 'mul', 'div']
    user_args = ['a', 'b']
    code = 'ARITH'

    def evaluate_sum(self):
        """
        func to sum two numbers
        """
        return self.args.a + self.args.b

    def evaluate_sub(self):
        """
        func to subtract two numbers
        """
        return self.args.a - self.args.b

    def evaluate_mul(self):
        """
        func to multiply two numbers
        """
        return self.args.a * self.args.b

    def evaluate_div(self):
        """
        func to divide two numbers
        """
        try:
            return self.args.a / self.args.b
        except:
            raise Exception(self.messages['ARITH_ERROR_DIVISIONBYZERO'])
