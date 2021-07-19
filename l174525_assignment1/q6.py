#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandasprint("\nNumber of nulls after filling self employed:",df.apply(lambda x: sum(x.isnull()),axis=0))


# In[2]:


df.head(7)


# In[3]:


df['LoanAmount_normalized'] = (df['LoanAmount'])/(df['LoanAmount'].std())


# In[5]:


print(df['LoanAmount'].hist(bins=20))


# In[6]:


print(df['LoanAmount_normalized'].hist(bins=20))


# In[7]:


df['ApplicantIncome_normalized'] = (df['ApplicantIncome'])/(df['ApplicantIncome'].std())


# In[8]:


print(df['ApplicantIncome'].hist(bins=20))


# In[9]:


print(df['ApplicantIncome_normalized'].hist(bins=20))


# In[ ]:




