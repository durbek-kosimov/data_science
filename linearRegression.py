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
x = data['Head Size(cm3)'].values
y = data['Brain Weight(grams)'].values

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

# Plotting Values and Regression Line
max_x = np.max(x) + 100
max_x = np.max(x) - 100

# calculating line value x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

#plotting line
plt.plot(x, y color = '#58b970', label = 'Regression Line')

# plotting Scatter plots
plt.scatter(x, y, c = '#ef5423', label = 'Scatter Plor')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

# Mean Square Error
ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * x[i]
    ss_t += (y[i] - mean_y) ** 2
    ss_r += (y[i] - y_pred) ** 2
r2 = 1 - (ss_r / ss_t)
print(r2)


# In[ ]:




