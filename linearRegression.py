#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pndas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figuresize'] = (20.0, 10.0)

#Read Data
data = pd.read_csv('headbrain.csv')
print(data.shape)
data.head()

# Collecting X and Y
x = data['Head Size(sm3)'].values
y = data['Brain Weight(gramms)'].values

# mean X and Y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Total number of values
m = len(x)

# Using the formula to calculate b1 and b2
numer = 0
denom = 0
for i in range(m):
    numer += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2
b1 = numer / denom # slope m
b0 = mean_y - (b1 * mean_x)
print(b1, b0)


# In[ ]:




