# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:57:07 2017

@author: a0229971
"""
import os
from unittest import TestCase,main
from calculator_as_plugin.multicalculator import MultiCalculator
from argparse import Namespace



class TestMultiCalculator(TestCase):

    def test_bridge(self):
        args = Namespace(operation=os.path.realpath(os.path.join(os.path.dirname(__file__),"test_data","file.txt")))
        MultiCalculator(args).bridge()
