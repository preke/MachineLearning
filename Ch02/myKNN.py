#coding:utf-8

#自己实现的约会网站配对的example

import numpy
from numpy import *

#训练

#read data, 返回数据和标签的numpy array
def readData(filename):
    fp = open(filename)
    arrayList = fp.readlines()
    dataSet = []
    labelSet = []
    d = dict()
    d['didntLike']  = 1
    d['smallDoses'] = 2
    d['largeDoses'] = 3
    for line in arrayList:
        line = line.strip()
        elems = line.split('\t')
        dataSet.append(elems[0:3])
        labelSet.append(int(d[elems[-1]]))

    dataSet = numpy.array(dataSet)
    labelSet = numpy.array(labelSet)
    #print labelSet
    return dataSet, labelSet


#略过画图
#归一化数据
def norm(dataSet):
    minival = dataSet.min(axis=0)
    print minival


if __name__ == '__main__':
    pass

#测试