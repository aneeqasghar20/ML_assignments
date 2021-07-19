#!/usr/bin/env python
# coding: utf-8

# In[181]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandas


# In[182]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[183]:


df['LoanAmount'].max()


# In[184]:


df['LoanAmount'].fillna(df['LoanAmount'].max(), inplace=True)


# In[185]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[186]:


print(df['Self_Employed'].value_counts())


# In[187]:


df['Self_Employed'].fillna('Yes',inplace=True)


# In[188]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[189]:


print(df['Gender'].value_counts())


# In[190]:


df['Gender'].fillna('Male',inplace=True)


# In[191]:


print(df['Married'].value_counts())


# In[192]:


df['Married'].fillna('Yes',inplace=True)


# In[193]:


print(df['Dependents'].value_counts())


# In[194]:


df['Dependents'].fillna(0,inplace=True)


# In[195]:


df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)


# In[196]:


print(df['Credit_History'].value_counts())


# In[197]:


df['Credit_History'].fillna(1.0,inplace=True)


# In[198]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[199]:


print(df['LoanAmount'].hist(bins=50))


# In[200]:


df.head(5)


# In[ ]:





# In[ ]:





# In[ ]:




