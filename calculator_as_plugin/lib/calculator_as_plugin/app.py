# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 13:20:46 2017

@author: a0229971
"""
import inspect,logging


class App:

    def __init__(self, *args, **kwargs):
        funcs = {'arg_parser': ['arr'], 'bridge': [], 'run': []}
        for func in list(funcs):
            if not(hasattr(self, func)):
                raise Exception(func+' not found')
            if not ('args' in list(inspect.signature(getattr(self,func)).parameters) or
                    'kwargs' in list(inspect.signature(getattr(self,func)).parameters)):
                if not list(inspect.signature(getattr(self,func)).parameters) == funcs[func]:
                    logging.error(func+' has parameters mismatch with super class')
                    raise Exception()
