#!/usr/bin/env python
# coding: utf-8

# Задание 1

# In[1]:


import numpy as np


# In[2]:


a = np.array(([1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]))


# In[3]:


mean_a = a.mean(axis = 0)


# In[4]:


mean_a


# Задание 2

# In[5]:


a_centered = a - mean_a


# In[6]:


a_centered


# Задание 3

# In[7]:


b = a_centered[0:, 1]
d = a_centered[0:, 0]


# In[8]:


a_centered_sp = np.dot(b,d)


# In[9]:


a_centered_sp


# In[10]:


a_centered_sp / a.shape


# In[11]:


cov = a_centered_sp / (a.shape[0]-1)


# In[12]:


cov


# Задание 4**

# In[13]:


cov1 = np.cov(a.T)


# In[14]:


cov1


# In[15]:


cov == cov1[0, 1]


# In[ ]:




