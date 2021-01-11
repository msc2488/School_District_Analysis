#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add the Pandas dependency.
import pandas as pd


# In[2]:


# Files to load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"


# In[3]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[4]:


#View first five rows of dataframe
school_data_df.head()


# In[5]:


#view last five rows of dataframe
scool_data_df.tail()


# In[6]:


#view last five rows of dataframe
school_data.df.tail()


# In[7]:


#view last five rows of dataframe
school_data_df.tail()


# In[8]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[ ]:




