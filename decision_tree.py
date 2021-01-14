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
    


# In[ ]:




