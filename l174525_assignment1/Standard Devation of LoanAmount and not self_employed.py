#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandas


# In[78]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[79]:


df['LoanAmount'].std()


# In[80]:


df['LoanAmount'].fillna(df['LoanAmount'].std(), inplace=True)


# In[81]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[82]:


print(df['Self_Employed'].value_counts())


# In[83]:


df['Self_Employed'].fillna('No',inplace=True)


# In[84]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[85]:


print(df['Gender'].value_counts())


# In[86]:


df['Gender'].fillna('Male',inplace=True)


# In[87]:


print(df['Married'].value_counts())


# In[88]:


df['Married'].fillna('Yes',inplace=True)


# In[89]:


print(df['Dependents'].value_counts())


# In[90]:


df['Dependents'].fillna(0,inplace=True)


# In[91]:


df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(), inplace=True)


# In[92]:


print(df['Credit_History'].value_counts())


# In[93]:


df['Credit_History'].fillna(1.0,inplace=True)


# In[94]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[95]:


print(df['LoanAmount'].hist(bins=50))


# In[96]:


df.head(5)


# In[ ]:





# In[ ]:





# In[ ]:




