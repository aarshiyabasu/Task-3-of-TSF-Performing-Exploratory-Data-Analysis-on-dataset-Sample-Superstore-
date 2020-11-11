#!/usr/bin/env python
# coding: utf-8
Task-3 Perform 'Exploratory Data Analysis' on dataset 'Sample Superstore'
# In[1]:


import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv('C:\\Users\\LENOVO\\Downloads\\SampleSuperstore.csv')


# In[4]:


data.head(20)


# In[5]:


data.describe()


# In[6]:



data.info()


# In[7]:


data.isnull().sum()


# In[8]:


data.duplicated().sum()


# In[9]:


data.drop_duplicates(inplace=True)


# In[11]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['State']
y=data['Sales']
ax.set_xlabel('State')
ax.set_ylabel('Sales')
ax.set_title('STATE WISE SALES DISTRIBUTION')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# In[12]:



fig,ax=plt.subplots(figsize=(30,12))
x=data['State']
y=data['Profit']
ax.set_xlabel('State')
ax.set_ylabel('Profit')
ax.set_title('STATE WISE PROFIT DISTRIBUTION')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# In[13]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['Region']
y=data['Sales']
ax.set_xlabel('Region')
ax.set_ylabel('Sales')
ax.set_title('REGION WISE PROFIT DISTRIBUTION')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# In[15]:


#REGION WISE CATEGORY CLASSIFICATION
plt.figure(figsize = (30, 12))
sns.countplot(x = 'Category', hue = 'Region', data = data, palette = 'rocket')
plt.xticks(rotation = 45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.xlabel('Categories', fontsize = 25)
plt.ylabel('', fontsize = 20)
plt.legend(loc = 5, fontsize = 20)


# In[18]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['Category']
y=data['Sales']
ax.set_xlabel('Category')
ax.set_ylabel('Sales')
ax.set_title('CATEGORY WISE SALES DISTRIBUTION')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# In[20]:


#CATEGORY WISE PROFIT DIST
plt.figure(figsize=(17,8))
sns.barplot(data['Category'],data['Profit'])
plt.show()


# In[21]:


sns.heatmap(data.corr(),annot=True)
plt.show()


# East region is the weakest part in terms of sales and profit. Furniture sector has lowest profit and the lowest sales. Eastern Region and the Furniture Sector can be considered as the weakest areas to be worked on to raise profits.
