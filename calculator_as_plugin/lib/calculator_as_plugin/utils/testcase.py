# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:46:23 2017

@author: a0229971
"""
from unittest import main, TestCase as TC


class TestCase(TC):
    """
    class to be imported while unittesting
    """
    mock_capture = None

    def setUp(self):
        """
        setUp fn is called before every single unit test fns
        """
        self.mock_capture = []

    def mock_function(self, name):
        def mock(*args, **kwargs):
            self.mock_capture.append(dict(name=name, args=args, kwargs=kwargs))
        return mock

    def run_mock(self, mock_object, mock_functions, test_function):
        mock_function_bkps = []
        for mock_function in mock_functions:
            mock_function_bkps.append(getattr(mock_object, mock_function))
            setattr(mock_object, mock_function, self.mock_function(mock_function))
        try:
            test_function()
        except:
            raise
        finally:
            for mock_function, mock_function_bkp in zip(mock_functions, mock_function_bkps):
                setattr(mock_object, mock_function, mock_function_bkp)
