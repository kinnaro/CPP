# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 18:45:51 2018

@author: Mindy
"""

from math import log, exp


class LaplaceEstimate(object):
    '''
    拉普拉斯平滑处理的贝叶斯估计
    '''
    
    def __init__(self):
        self.d = {}     # [词-词频]的map
        self.total = 0.0    # 全部词的词频
        self.none = 1   # 当一个词不存在的时候，它的词频（等于0+1）
        
    def exists(self, key):
        return key in self.d
    
    def getsum(self):
        return self.total
    
    
    
    