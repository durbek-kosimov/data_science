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


# In[ ]:




