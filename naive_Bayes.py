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

