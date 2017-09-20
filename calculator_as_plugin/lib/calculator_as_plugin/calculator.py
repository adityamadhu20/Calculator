# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:08:22 2017

@author: a0229971
"""
import logging
import argparse
import sys
import calculator_as_plugin.plugins as plugins

logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)


class Calculator:

    args = None
    un_args = None
    operation = None
    _operations = None

    def __init__(self, args=None, un_args = None):

        self._operations = []
        for k, v in plugins.operations.items():
            self._operations += v.operations
        self.args = args

    def arg_parser(self, arr):
        parser = argparse.ArgumentParser(description='Calculator')
        group = parser.add_mutually_exclusive_group(required=True)
        for operation in self._operations:
            group.add_argument('--'+operation, action='store_true',
                               help=operation+' calculation of two numbers')
        args, un_args = parser.parse_known_args(arr)
        self.un_args = un_args
        self.args = vars(args)
        print(self.args)

    def bridge(self):
        for key in self._operations:
            if self.args.get(key):
                for k, v in plugins.operations.items():
                    if key in v.operations:
                        return getattr(v, 'run')(self.un_args, key)

    def run(self):
        self.arg_parser(sys.argv[1:])
        logging.info(self.bridge())
