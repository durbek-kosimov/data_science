#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Logistic Regression Project 
# 
# In this project we will be working with a fake advertising data set, indicating whether or not a particular internet user clicked on an Advertisement. We will try to create a model that will predict whether or not they will click on an ad based off the features of that user.
# 
# This data set contains the following features:
# 
# * 'Daily Time Spent on Site': consumer time on site in minutes
# * 'Age': cutomer age in years
# * 'Area Income': Avg. Income of geographical area of consumer
# * 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
# * 'Ad Topic Line': Headline of the advertisement
# * 'City': City of consumer
# * 'Male': Whether or not consumer was male
# * 'Country': Country of consumer
# * 'Timestamp': Time at which consumer clicked on Ad or closed window
# * 'Clicked on Ad': 0 or 1 indicated clicking on Ad
# 
# ## Import Libraries
# 
# **Import a few libraries you think you'll need (Or just import them as you go along!)**

# In[64]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# **Read in the advertising.csv file and set it to a data frame called ad_data.**

# In[65]:


ad_data = pd.read_csv('advertising.csv')


# **Check the head of ad_data**

# In[66]:


ad_data.head()


# ** Use info and describe() on ad_data**

# In[67]:


ad_data.info()


# In[68]:


ad_data.describe()


# ## Exploratory Data Analysis
# 
# Let's use seaborn to explore the data!
# 
# Try recreating the plots shown below!
# 
# ** Create a histogram of the Age**

# In[69]:


sns.distplot(ad_data['Age'].dropna(), kde=False, bins=30)


# In[70]:


ad_data['Age'].plot.hist(bins=30)


# In[ ]:





# **Create a jointplot showing Area Income versus Age.**

# In[71]:


ad_data.columns


# In[72]:


sns.jointplot(x='Age', y='Area Income', data=ad_data)


# In[ ]:





# **Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.**

# In[73]:


ad_data.columns


# In[74]:


sns.jointplot(x='Age', y='Daily Time Spent on Site', data=ad_data, kind='kde', color='r')


# In[ ]:





# ** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**

# In[75]:


ad_data.columns


# In[76]:


sns.jointplot(x='Daily Internet Usage', y='Daily Time Spent on Site',data=ad_data,color='g')


# In[ ]:





# ** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**

# In[77]:


sns.pairplot(ad_data, hue='Clicked on Ad')


# In[ ]:





# # Logistic Regression
# 
# Now it's time to do a train test split, and train our model!
# 
# You'll have the freedom here to choose columns that you want to train on!

# ** Split the data into training set and testing set using train_test_split**

# In[78]:


ad_data.columns


# In[79]:


ad_data.head()


# In[80]:


X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage','Male']]


# In[81]:


y = ad_data['Clicked on Ad']


# ** Train and fit a logistic regression model on the training set.**

# In[82]:


from sklearn.model_selection import train_test_split


# In[83]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# ## Predictions and Evaluations
# ** Now predict values for the testing data.**

# In[84]:


from sklearn.linear_model import LogisticRegression


# ** Create a classification report for the model.**

# In[85]:


logmodel = LogisticRegression()


# In[86]:


logmodel.fit(X_train, y_train)


# In[87]:


prediction = logmodel.predict(X_test)


# In[90]:


from sklearn.metrics import classification_report, confusion_matrix


# In[91]:


print(classification_report(y_test, prediction))
print(confusion_matrix(y_test, prediction))


# In[ ]:





# ## Great Job!
