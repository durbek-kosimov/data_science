#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[9]:


x = np.linspace(0, 5, 11)
y = x**2
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()


# In[12]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()


# ## OO Plot

# In[18]:


fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')


# In[19]:


fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes.set_title('Larger Plot')

axes2.plot(y,x)
axes.set_title('Smaller Plot')


# In[22]:


fig, axes = plt.subplots()
axes.plot(x,y)

fig, axes = plt.subplots(nrows = 1, ncols = 2)
for current_ax in axes:
    current_ax.plot(x,y)
# axes.plot(x,y)


# In[25]:


fig, axes = plt.subplots(nrows = 3, ncols = 3)
plt.tight_layout()


# In[28]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)
axes[0].plot(x,y)
# axes[0].plot(x,y)


# In[29]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)
axes[0].plot(x,y)
axes[1].plot(y,x)


# ## Figure Size and DPI

# In[36]:


fig, axes = plt.subplots()
# fig = plt.figure(figsize = (8,2))
# fig = plt.figure(figsize = (8,2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x,y)


# In[38]:


fig, axes = plt.subplots(figsize = (8,2))
axes.plot(x,y)


# In[43]:


fig, axes = plt.subplots(nrows=2, ncols=1, figsize = (8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# In[44]:


fig.savefig('My_picture.png', dpi=200)


# In[47]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label='x Squared')
ax.plot(x,x**3, label='x Cubed')
ax.legend()
# ax.legend(loc=0)
# ax.legend(loc=(0.1,0.1))


# In[ ]:




