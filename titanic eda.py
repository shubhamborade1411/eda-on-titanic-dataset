#!/usr/bin/env python
# coding: utf-8

# In[137]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[138]:


import pandas as pd
import os


os.chdir('C:\\Users\\Shubham\\Downloads')
df=pd.read_csv('train.csv')
df


# In[139]:


df.info()


# In[140]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[141]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',data=df)


# In[142]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue="Sex",data=df,palette='RdBu_r')


# In[143]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue="Pclass",data=df,palette='rainbow')


# In[144]:


sns.distplot(df['Age'].dropna(),kde=False,color='darkred',bins=40)


# In[145]:


sns.countplot(x='SibSp',data=df)


# In[146]:


sns.countplot(x='SibSp',hue='Survived',data=df)


# In[147]:


sns.boxplot(x="Pclass",y='Age',data=df)


# In[148]:


def ageit(age):
    if age<10:
        return 1
    elif age>10 and age<30:
        return 2
    elif age>30 and age<50:
        return 3
    else:
        return 4
    
        


# In[149]:


df['Age']=df['Age'].apply(lambda x: ageit(x))


# In[ ]:





# In[150]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[151]:


df.drop('Cabin',axis=1,inplace=True)


# In[152]:


df['Embarked']=df['Embarked'].fillna("S")


# In[153]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[154]:


df['Embarked']=df['Embarked'].map({'S':1,'C':2,'Q':3})


# In[156]:


df


# In[ ]:




