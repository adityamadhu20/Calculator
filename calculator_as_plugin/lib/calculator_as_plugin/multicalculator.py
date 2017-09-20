# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:08:22 2017

@author: a0229971
"""
import logging
import argparse
import shlex
import sys
import calculator_as_plugin.plugins as plugins

logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)


class MultiCalculator:

    args = None
    un_args = None
    operation = None
    _operations = None

    def __init__(self, args=None):

        self._operations = []
        for k, v in plugins.operations.items():
            self._operations += v.operations
        self.args = args

    def arg_parser(self, arr):
        parser = argparse.ArgumentParser(description='Calculator')
        parser.add_argument('--operation',required=True, help='list of operations ')
        self.args = parser.parse_args(arr)

    def arg_parser_line(self, arr):
        parser = argparse.ArgumentParser(description='Calculator')
        group = parser.add_mutually_exclusive_group(required=True)
        for operation in self._operations:
            group.add_argument('--'+operation, action='store_true',
                               help=operation+' calculation of two numbers')
        parser.add_argument('--condition',default='True',required=False, help='can provide python compatible expression')
        return parser.parse_known_args(arr)

    def bridge(self):

        with open(self.args.operation) as f:
            result_dict = {}
            result = 0
            for index, line in enumerate(f.readlines()):
                line = line.format(**result_dict)
                args, un_args = self.arg_parser_line(shlex.split(line))
                if eval(args.condition, result_dict):
                    key = next(filter(lambda x:getattr(args,x),self._operations))
                    v = next(filter(lambda x:key in x.operations,plugins.operations.values()))
                    result,output = getattr(v, 'run')(un_args, key)
                    logging.info(output)
                    result_dict['previous_result'] = result
                    result_dict['step{index}_result'.format(index=index)] = result
                else:
                    result_dict['step{index}_result'.format(index=index)] = None

    def run(self):
        self.arg_parser(sys.argv[1:])
        self.bridge()
