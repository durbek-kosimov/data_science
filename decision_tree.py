#!/usr/bin/env python
# coding: utf-8

# In[5]:


training_data = [
    ['Green', 3, 'Mango'],
    ['Yellow', 3, 'Mango'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yello', 3, 'Lemon'],
]

# Column labels
# These are used only to print the tree

header = ['color', 'diameter', 'label']

def unique_vals(rows, col):
    """Find the unique values for a column in a dataset"""
    return set([row[col] for row in rows])

# Demo
# unique_vals(training_data, 0)
# unique_vals(training_data, 1)

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {} # a dictionary label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column.
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts
# Demo
# class_counts(training_data)
# 

def in_numeric(value):
    """Test if a value is numeric"""
    return isinstance(value, int) or isinstance(value, float)
# Demo
# is_numeric(7)
# is_numeric('Red')
# 

class Question:
    """A Question is used to partition a dataset.
    This class just records a 'column numbers'
    (e.g., 0 for color) and a 'column value' (e.g.,
    Gree). The 'match' method is used to compare the 
    feature value in an example to the feature value
    atarted in the question. See the demo bellow.
    """
    def __init__(self, column, value):
        self.column  column
        self.value = value
        
    def match(self, example):
        # Compare the feature value in an example
        # to the feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value

def gini(rows):
    """Calculate the Gini Impurity for list of rows."""
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity

# Demo
# Let's look at some example to understand how Gini Impurity works.
def info_gain(left, right, current_uncertainty):
    """Information Gain.
    The uncertainty of the starting node, 
    minus the weighted impurity of two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

# Demo
# Calculate the uncertainty of our training data.
# current_uncertainty  gini(training_data)

# How much information do we gain by partitioning on 'Green'?
# true_rows, false_rows = partition(training_data, Question(0, 'Green'))
# info_gain(true_rows, false_rows, current_uncertainty)

# What about if we partitioned on 'Red' instead?
# true_rows, false_rows = partition(training_data, Question(0, 'Red'))
# info_gain(true_rows, false_rows, current_uncertainty)


# In[ ]:




