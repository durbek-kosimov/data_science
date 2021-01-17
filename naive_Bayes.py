#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import math
import random

def loadCsv(filename):
    lines = csv.reader(open(r'/home/dmint/pima-indians-diabets.data.csv'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]] # convert int into float
    return dataset

def splitDataset(dataset, splitRation):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return (trainSet.copy)

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

