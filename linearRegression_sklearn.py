#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cannot use Rank 1 matrix in Scikit Learn
x = x.reshape((m, 1))

# Creating Model
reg = LinearRegression()

# Fitting Training Data
reg = reg.fit(x, y)

# y Prediction
y_pred = reg.predict(x)

# calculating R2 score
r2_score = reg.score(x, y)
print(r2_score)


# In[ ]:




