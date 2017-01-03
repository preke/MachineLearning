# coding: utf-8

from math import log
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

# 以分类结果（最后一列）作为划分
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

# 返回一个子数据集，数据集中axis项的特征都为value，并且删除axis这一列
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for vec in dataSet:
        if vec[axis] == value:
            reducedVec = vec[:axis]
            reducedVec.extend(vec[axis+1:])
            retDataSet.append(reducedVec)

    return retDataSet


# 选出信息增益最大的分类标签 (在此用ID3算法)
# 计算每个分类标签的条件熵，然后再算信息增益
def ChooseBestFeature(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeatureIndex = -1

    for i in range(numFeatures):
        featList = [example[i] for example in dataSet] # 取出特征的一列
        uniqueVals = set(featList)
        newEntropy = 0.0
        for val in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, val)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeatureIndex  = i
    return bestFeatureIndex

# 开始递归构建决策树



