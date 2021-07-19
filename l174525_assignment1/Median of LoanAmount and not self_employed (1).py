#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandas


# In[2]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[33]:


df['LoanAmount'].median()


# In[30]:


df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)


# In[31]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[8]:


print(df['Self_Employed'].value_counts())


# In[9]:


df['Self_Employed'].fillna('No',inplace=True)


# In[10]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[11]:


print(df['Gender'].value_counts())


# In[14]:


df['Gender'].fillna('Male',inplace=True)


# In[15]:


print(df['Married'].value_counts())


# In[16]:


df['Married'].fillna('Yes',inplace=True)


# In[17]:


print(df['Dependents'].value_counts())


# In[25]:


df['Dependents'].fillna(0,inplace=True)


# In[22]:


df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)


# In[23]:


print(df['Credit_History'].value_counts())


# In[27]:


df['Credit_History'].fillna(1.0,inplace=True)


# In[32]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[34]:


print(df['LoanAmount'].hist(bins=50))


# In[ ]:




