#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('USA_Housing.csv')


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.columns


# In[9]:


sns.pairplot(df)


# In[10]:


sns.distplot(df['Price'])


# In[11]:


df.corr()


# In[12]:


sns.heatmap(df.corr())


# In[13]:


sns.heatmap(df.corr(), annot=True)


# In[14]:


df.columns


# In[15]:


X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]


# In[16]:


y = df['Price']


# In[17]:


from sklearn.model_selection import train_test_split


# In[18]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# In[19]:


from sklearn.linear_model import LinearRegression


# In[20]:


lm = LinearRegression()


# In[21]:


lm.fit(X_train, y_train)


# In[22]:


print(lm.intercept_)


# In[23]:


lm.coef_


# In[ ]:




