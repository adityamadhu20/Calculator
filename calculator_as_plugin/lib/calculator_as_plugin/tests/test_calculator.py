# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:08:45 2017

@author: a0229971
"""
import shlex
from calculator_as_plugin.calculator import Calculator
from calculator_as_plugin.utils import TestCase, main
from calculator_as_plugin.plugins.plugin_arithmetic import Plugin as PluginArithmetic
from calculator_as_plugin.plugins.plugin_arithmetic import Plugin as PluginTrignometry

class TestCalculator(TestCase):

    def test_arg_parser(self):
        calculator = Calculator()
        operations = ['sum', 'sub', 'mul', 'div', 'sin', 'cos', 'tan']
        operation_dict = {}
        for operation in operations:
            operation_dict[operation] = False

        for operation in operations:
            operation_dict[operation] = True
            calculator.arg_parser(shlex.split('--a 3 --b 4 --'+operation))
            self.assertEqual(operation_dict, calculator.args)
            self.assertEqual(['--a','3','--b','4'],calculator.un_args)
            operation_dict[operation] = False


    def generic_bridge(self,operation):
        calculator_obj = Calculator(args={operation:True})
        if operation in PluginTrignometry.operations:
            calculator_obj.un_args=['-a','10']
            plugin_trignometry_obj = PluginTrignometry(a=10)
            self.run_mock(plugin_trignometry_obj, ['run'], calculator_obj.bridge)
            self.assertTrue(self.mock_capture)

        if operation in PluginArithmetic.operations:
            print("inside else")
            calculator_obj.un_args=['-a','10','-b','20']
            print(calculator_obj.bridge())
            plugin_arithmetic_obj = PluginArithmetic(a=10, b=20)
            self.run_mock(plugin_arithmetic_obj, ['run'], plugin_calculator_obj.bridge)
            self.assertTrue(self.mock_capture)


    def test_bridge_plugin_arithmetic(self):
        self.generic_bridge('sum')

    def test_bridge_plugin_trignometry(self):
        self.generic_bridge('sin')


if __name__ == "__main__":
    main()
