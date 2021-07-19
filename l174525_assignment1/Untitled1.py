#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("D:\Train file.csv") #Reading the dataset in a dataframe using Pandas


# In[2]:


df.head(10)


# In[3]:


df.describe()


# In[4]:


df['Property_Area'].value_counts()


# In[5]:


df['ApplicantIncome'].hist(bins=50)


# In[6]:


df.boxplot(column='ApplicantIncome')


# In[7]:


df.boxplot(column='ApplicantIncome', by = 'Education')


# In[8]:


df['LoanAmount'].hist(bins=50)


# In[9]:


df.boxplot(column='LoanAmount')


# In[10]:


temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x:
x.map ({'Y':1,'N':0}).mean())
print('Frequency Table for Credit History:')
print(temp1)
print ('\nProbility of getting loan for each Credit History class:')
print(temp2)


# In[11]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')
ax2 = fig.add_subplot(122)
temp2.plot(kind = 'bar')
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by credit history")


# In[12]:


temp3 = pd.crosstab(df['Credit_History'], df['Loan_Status'])
temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)


# In[13]:


df.apply(lambda x: sum(x.isnull()),axis=0)


# In[14]:


df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)


# In[15]:


print("\nNumber of nulls after filling self employed:\n",df.apply(lambda x: sum(x.isnull()),axis=0))


# In[16]:


df['LoanAmount_log'] = np.log(df['LoanAmount'])
print(df['LoanAmount_log'].hist(bins=20))


# In[17]:


df['Self_Employed'].value_counts()


# In[18]:


df['Self_Employed'].fillna('No',inplace=True)


# In[19]:


print("\nNumber of nulls after filling Self_Employed column:\n",df.apply(lambda x: sum(x.isnull()),axis=0))


# In[20]:


df['LoanAmount_log'] = np.log(df['LoanAmount'])
df['LoanAmount_log'].hist(bins=20)


# In[21]:


df['TotalIncome'] = df['ApplicantIncome'] +
df['CoapplicantIncome'] df['TotalIncome_log'] =
np.log(df['TotalIncome']) df['LoanAmount_log'].hist(bins=20)


# In[22]:


df['TotalIncome'] = df['ApplicantIncome'] +df['CoapplicantIncome'] df['TotalIncome_log'] =np.log(df['TotalIncome']) df['LoanAmount_log'].hist(bins=20)


# In[ ]:




