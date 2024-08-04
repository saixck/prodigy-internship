#!/usr/bin/env python
# coding: utf-8

# # Aim: Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as distribution of ages or genders in a population  

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("E:\downloads\downloads chrome\Insurance Premium.csv")


# In[2]:


df.head(5)


# In[3]:


df.info


# In[4]:


df.isnull().sum()


# In[5]:


df.columns


# In[6]:


df.dtypes


# # 1.Categorical Variable (Bar Chart)

# In[7]:


plt.figure(figsize=(6, 4))  
Gender_colors = {'male': 'pink', 'female': 'skyblue'}
df['Gender'].value_counts().plot(kind='bar', color=df['Gender'].map(Gender_colors))
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender')
plt.show()


# #  Continuous Variable (Histogram):

# In[8]:


plt.figure(figsize=(10, 4))  
plt.hist(df['Age'], bins=15,edgecolor='black')  
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()


# In[37]:


df1 = df[df['Smoker'] == 'no'
average_BMI = df1.groupby('Gender')['BMI'].sum()
average_BMI_positions = range(len(average_BMI))  # Create positions 0, 1, 2, ...

# Create bar chart
plt.figure(figsize=(5, 6))
plt.bar(average_BMI_positions, average_BMI)  # Use positions for x-axis
plt.xlabel('Gender')
plt.ylabel('BMI')
plt.title('gender by BMI of non smoker')
plt.xticks(average_BMI_positions, average_BMI.index, rotation=0)  # Set x-axis labels with positions
plt.show()

filtered_df = df[df['Smoker'] == 'yes']
average_BMI = filtered_df.groupby('Gender')['BMI'].sum()

# Get positions for each sales method (categorical data needs specific positioning)
average_BMI_positions = range(len(average_BMI))  # Create positions 0, 1, 2, ...

# Create bar chart
plt.figure(figsize=(5, 6))
plt.bar(average_BMI_positions, average_BMI)  # Use positions for x-axis
plt.xlabel('Gender')
plt.ylabel('BMI')
plt.title('gerder by BMI of smokers')
plt.xticks(average_BMI_positions, average_BMI.index, rotation=0)  # Set x-axis labels with positions
plt.show()]

