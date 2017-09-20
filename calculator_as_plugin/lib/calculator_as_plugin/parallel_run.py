# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:07:45 2017

@author: a0229971
"""
import os,subprocess

processlist = []
directory = os.getcwd()
for folder in os.listdir(directory):
    folder = os.path.join(directory, folder)
    print(folder)
    if (os.path.isdir(folder)):
        os.system('dir {folder}'.format(folder=folder))
        processobj = subprocess.Popen("echo"+folder,shell='True',stdout=subprocess.PIPE)
        processlist.append(processobj)
for process in processlist:
    process.wait()

