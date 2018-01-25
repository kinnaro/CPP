# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:24:21 2018

@author: Mindy
"""

T = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]

class node:
    def __init__(self, point):
        self.left = None
        self.right = None
        self.point = point
        pass

# data 数据的中位数，返回坐标和当前位置
def median(lst):
    m = int(len(lst) / 2)
    return lst[m], m

# 构建树
def build_kdtree(data, d):
    data = sorted(data, key=lambda x: x[d]) # data中
    p, m = median(data) # P为中位数在data中的坐标，m为当前中位数值
    tree = node(p)  # 构建各根节点
    
    del data[m]
    print(data, p)
    
    # 构建树的左、右节点
    if m > 0: tree.left = build_kdtree(data[:m], not d)
    if len(data) > 1: tree.right = build_kdtree(data[m:], not d)
    return tree

kd_tree = build_kdtree(T, 0)
print(kd_tree)