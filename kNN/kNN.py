# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:33:42 2017

@author: Mindy
"""

from numpy import *
import operator
import autoNorm

def creatDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

if __name__ == '__main__':
    creatDataSet()
    