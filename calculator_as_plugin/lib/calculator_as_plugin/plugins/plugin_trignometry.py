# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:38:45 2017

@author: a0229971
"""
import math
from .plugin import Plugin as BasePlugin


class Plugin(BasePlugin):

    operations = ['sin', 'cos', 'tan']
    user_args = ['a']
    code = 'TRIG'

    def evaluate_sin(self):
        return math.sin(self.args.a)

    def evaluate_cos(self):
        return math.cos(self.args.a)

    def evaluate_tan(self):
        return math.tan(self.args.a)


