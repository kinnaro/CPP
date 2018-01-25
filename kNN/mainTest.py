# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 11:06:34 2017

@author: Mindy
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:44:51 2017

@author: Mindy
"""
import classify0
from numpy import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #加载数据并归一化
    datingDataMat, datingLabels = classify0.file2matrix('P:\zmfTest\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat, ranges, minVals = classify0.autoNorm(datingDataMat)
    print(normMat)
    classify0.classifyPerson()
   # print(ranges)
   # print(minVals)
   
'''   
    #画图 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(normMat[:,1], normMat[:,2], 8.0*array(datingLabels), 8.0*array(datingLabels))
    plt.xlabel(u'玩视频游戏所耗时间百分比', fontproperties='SimHei')
    plt.ylabel(u'每周消费的冰激凌公升数', fontproperties='SimHei')
    plt.show()
  
   #测试 
    classify0.datingClassTest()
'''      


    
    
