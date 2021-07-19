#!/usr/bin/env python
# coding: utf-8

# In[1]:


ipython notebook --pylab=inline


# In[2]:


6+2


# In[3]:


import matplotlib
plot(arange(5))


# In[4]:


import matplotlib as m
m.plot(arange(5))


# In[5]:


from matplotlib import *
plot(arange(5))


# In[6]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset
in a dataframe using Pandas


# In[7]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandas


# In[8]:


df.head(10)


# In[9]:


df.describe()


# In[10]:


df['Property_Area'].value_counts()


# In[11]:





# In[12]:


dfname['Credit_History']


# In[13]:


dfname['Credit_History'].value_counts()


# In[14]:


df.boxplot(column='ApplicantIncome')


# In[15]:


df.boxplot(column='ApplicantIncome', by = 'Education')


# In[16]:


df['LoanAmount'].hist(bins=50)


# In[17]:


temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x:
x.map ({'Y':1,'N':0}).mean())
print 'Frequency Table for Credit History:'
print temp1
print '\nProbility of getting loan for each Credit History
class:' print temp2


# In[20]:


temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x:
x.map ({'Y':1,'N':0}).mean())
print('Frequency Table for Credit History:')
print(temp1)
print ('\nProbility of getting loan for each Credit History')
class:' print temp2


# In[22]:


temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x:
x.map ({'Y':1,'N':0}).mean())
print('Frequency Table for Credit History:')
print(temp1)
print ('\nProbility of getting loan for each Credit History class:')
print(temp2)


# In[23]:


table = df.pivot_table(values='LoanAmount', index='Self_Employed' ,columns='Education',aggfu nc=np.median)


# In[24]:


table = df.pivot_table(values='LoanAmount', index='Self_Employed' ,columns='Education', nc=np.median)


# In[25]:


table = df.pivot_table(values='LoanAmount', index='Self_Employed' ,columns='Education')


# In[ ]:





# In[26]:


print(table)


# In[ ]:




