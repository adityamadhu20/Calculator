# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:34:56 2017

@author: a0229971
"""

from utils import TestCase, main
from plugins.plugin_arithmetic import Plugin


class TestPluginArithmetic:
    def test_evaluate_sum(self):
        self.assertEqual(Plugin().evaluate_sum(2,3))


