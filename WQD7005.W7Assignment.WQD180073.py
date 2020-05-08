#!/usr/bin/env python
# coding: utf-8

# WQD7005 Data Mining
# Week 7 Online Assessment (8th May 2020)
# 
# Yap Hui Hsing, WQD180073 (17039525/2)
# 
# Team member: Har Wai San, WQD180025 (17051470/1)
# 

# ## 0. Import Lib

# In[1]:


import pandas as pd
import numpy as np


# ## 1. Data Exploration
# ### 1.1 Import the dataset

# In[2]:


# Read data from file 'Survey_2016.xlsx' 
df = pd.read_csv('output.(6 May).csv', names=['Date','Sector_Number','Sector_Name','Stock_Code','Stock_Name','Ref','Open','Last','Change','Change_%', 'Volume'])
print(df.shape)


# In[3]:


# Using .head() method to view the first few records of the data set
df.head()


# In[4]:


# using the dtypes() method to display the different datatypes available
df.dtypes


# ### 1.2 Descriptive Dataset

# In[5]:


# Generate descriptive statistics that summarize of all observed features and labels 
# Numeric columns
df.describe(include=[np.number])


# In[6]:


# Object columns
df.describe(include=[np.object])


# In[7]:


#Count Unique value in all dataset columns
df.nunique()


# In[8]:


df['Sector_Number'].unique()


# In[9]:


df['Sector_Name'].unique()


# In[10]:


df['Stock_Code'].unique()


# In[11]:


df['Stock_Name'].unique()


# ## 2. Data Cleaning

# ### 2.1 Check for missing values

# In[12]:


# check on the missing value
df.isnull().sum() 
# Output shows there is no missing value in the data


# In[13]:


# check on the missing value
df.notnull().head()

