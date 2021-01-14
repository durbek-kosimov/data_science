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

# def class_counts()
# 

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


# In[ ]:




