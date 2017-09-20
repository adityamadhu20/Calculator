# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:17:39 2017

@author: a0229971
"""
import argparse
from configobj import ConfigObj
import os


class Plugin:

    args = None

    def __init__(self,a=None):

        self.messages = ConfigObj(os.path.realpath(os.path.join(
                 os.path.dirname(__file__), 'config.ini')))

        for operation in self.operations:
            function = 'evaluate_'+operation
            if not hasattr(self,function):
                raise Exception(self.messages['PLUGIN_ERROR_FUNCTION_NOT_FOUND'].format(function=function))


    def parser(self, un_arr):
        parser = argparse.ArgumentParser()
        for arg in self.user_args:
            parser.add_argument('--'+arg, type=float, required=True, help='Argument: '+arg)
        self.args = parser.parse_args(un_arr)

    def bridge(self):
        return getattr(self, 'evaluate_'+self.operation)()

    def run(self, un_arr, operation):
        self.operation = operation
        self.parser(un_arr)
        result = self.bridge()
        output = self.messages[self.code+'_INFO_OUTPUT'].format(operation=self.operation, result=result, **vars(self.args))
        return result,output
