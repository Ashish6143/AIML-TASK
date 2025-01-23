#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("Universities.csv")
df


# In[3]:


sal = pd.read_csv("Salaries.csv")
sal


# In[4]:


np.mean(df["SAT"])


# In[5]:


np.median(df["SAT"])


# In[6]:


np.median(df["Expenses"])


# In[7]:


np.std(df["GradRate"])


# In[8]:


np.var(df["SFRatio"])


# In[9]:


df.describe()


# In[19]:


# Visualize the GradRate 
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


plt.figure(figsize=(6,3))
plt.title("Graduation Rate")
plt.hist(df["GradRate"])


# In[24]:


s = [20,15,10,25,30,35,28,150,200]
scores = pd.Series(s)
scores


# In[26]:


plt.boxplot(scores,)


# In[ ]:





# In[28]:


s = [20,15,10,25,30,35,28,40,45,60,150,200]
scores = pd.Series(s)
scores


# In[ ]:





# In[30]:


plt.boxplot(scores)


# In[34]:


plt.figure(figsize=(6,2))
plt.title("Box plot for SAT Score")
plt.boxplot(df["SAT"], vert = False)


# In[ ]:




