# -*- coding: utf-8 -*-

"""
Created on Mon Dec 18 15:12:51 2017

@author: Mindy
"""

from numpy import * 
import operator
import matplotlib
import matplotlib.pyplot as plt


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 得到数组的行数。即知道有几个训练数据
    # tile:numpy中的函数。tile将原来的一个数组，扩充成了4个一样的数组
    # diffMat得到了目标与训练数值之间的差值
    print("111", dataSetSize)
    diffMat = tile(inX, (dataSetSize,1)) - dataSet  
    print("333", diffMat)
    sqDiffMat = diffMat ** 2  # 各个元素分别平方
    sqDistances = sqDiffMat.sum(axis=1) # 对应列相加，得到每一个距离的平方
    distances = sqDistances ** 0.5  # 开方，得到距离
    sortedDistIndicies = distances.argsort()    # 升序排列
    
    # 选择距离最小的K个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    
    # 排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# 将文本记录到转换numPy的解析程序
def file2matrix(filename):
    #打开文件并得到文件行数
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    #创建返回的numPy矩阵
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index =0
    #解析文件数据到列表
    for line in arrayOLines:
        line = line.strip()
        listFormLine = line.split('\t')
        returnMat[index,:] = listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))
        index += 1
    return returnMat, classLabelVector

# 数据归一化
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals
# 测试
def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('P:\zmfTest\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 3)
        print ("the classifier come back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])) 
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print ("the total error rate is: %f" % (errorCount/float(numTestVecs))) 
# 预测
def classifyPerson():
    resultList = ['渣男', '还不错', '男神']
    percentTats = float(input("打游戏的时间百分比？"))
    ffMiles = float(input("每年里程数？"))
    iceCream = float(input("给妹子买花数？"))
    datingDataMat, datingLabels = file2matrix('P:\zmfTest\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print(classifierResult)
    print("您可能喜欢的程度是：", resultList[classifierResult - 1])
 
'''
if __name__ == '__main__':
    datingDataMat, datingLabels = file2matrix('P:\zmfTest\machinelearninginaction\Ch02\datingTestSet2.txt')
    #print(datingDataMat)
    #print(datingLabels[0:20])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 8.0*array(datingLabels), 8.0*array(datingLabels))
    plt.xlabel(u'玩视频游戏所耗时间百分比', fontproperties='SimHei')
    plt.ylabel(u'每周消费的冰激凌公升数', fontproperties='SimHei')
    plt.show()
'''
    
    