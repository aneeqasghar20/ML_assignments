#!/usr/bin/env python
# coding: utf-8

# In[161]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandas


# In[162]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[163]:


df['LoanAmount'].max()


# In[164]:


df['LoanAmount'].fillna(df['LoanAmount'].max(), inplace=True)


# In[165]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[166]:


print(df['Self_Employed'].value_counts())


# In[167]:


df['Self_Employed'].fillna('No',inplace=True)


# In[168]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[169]:


print(df['Gender'].value_counts())


# In[170]:


df['Gender'].fillna('Male',inplace=True)


# In[171]:


print(df['Married'].value_counts())


# In[172]:


df['Married'].fillna('Yes',inplace=True)


# In[173]:


print(df['Dependents'].value_counts())


# In[174]:


df['Dependents'].fillna(0,inplace=True)


# In[175]:


df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)


# In[176]:


print(df['Credit_History'].value_counts())


# In[177]:


df['Credit_History'].fillna(1.0,inplace=True)


# In[178]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[179]:


print(df['LoanAmount'].hist(bins=50))


# In[180]:


df.head(5)


# In[ ]:





# In[ ]:





# In[ ]:




