import os
import importlib
list_of_files = os.listdir(os.path.dirname(__file__))
operations = {}

#def init():
for filename in list_of_files:
    if filename.startswith('plugin_') and filename.endswith('.py'):
        filename = filename.split('.py')[0]
        file_import = importlib.import_module('calculator_as_plugin.plugins.'+filename)
        operations[filename] = file_import.Plugin()
#init()
