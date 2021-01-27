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


# In[24]:


X_train.columns


# In[25]:


cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])


# In[26]:


cdf


# In[27]:


from sklearn.datasets import load_boston


# In[28]:


boston = load_boston()


# In[29]:


boston.keys()


# In[30]:


print(boston['DESCR'])


# In[31]:


print(boston['data'])


# In[32]:


print(boston['feature_names'])


# In[33]:


print(boston['target'])


# ## Predictions

# In[34]:


predictions = lm.predict(X_test) # X-test is a feature


# In[35]:


predictions # predictions of prices of house


# In[36]:


y_test


# In[37]:


plt.scatter(y_test, predictions)


# In[38]:


sns.distplot((y_test-predictions))


# In[39]:


from sklearn import metrics


# In[40]:


metrics.mean_absolute_error(y_test, predictions)


# In[41]:


metrics.mean_squared_error(y_test, predictions)


# In[42]:


np.sqrt(metrics.mean_squared_error(y_test, predictions))


# In[ ]:




