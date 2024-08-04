#!/usr/bin/env python
# coding: utf-8

# # Aim: To perform data cleaning and EDA on a dataset of your choice and explore relationships and patterns/trends in the data.

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[208]:


data = pd.read_csv('D:/hp/Documents/prodigy internship/task 2/data_sales (2).csv')


# In[210]:



df.head()


# In[211]:


data.columns


# In[ ]:





# In[212]:


data.info()


# In[213]:


data.describe()


# In[214]:


## missing values


# In[215]:


data.shape


# In[216]:


data.isnull().sum()


# In[217]:


[features for features in data.columns if data[features].isnull().sum()>0]

Observation: column "price per unit" has 2 rows with missing values.
# In[218]:


df= data.dropna()
df.head()


# In[170]:


df.isnull().sum()

we have removed the rows with missing values.
# In[187]:


df.dtypes


# In[181]:


plt.figure(figsize=(18,10))
sns.countplot(y=df['Region'])
plt.show()


# In[182]:


plt.figure(figsize=(15,15))
sns.countplot(y=df['City'])
plt.show()

observation:
In the above plots we can observe that the west & northeast region has the highest sales 
# In[183]:


## Pie Chart- Top 3 products
Product_names=df.Product.value_counts().index
Product_val=df.Product.value_counts().values
percentages = (df.Product.value_counts().head(3) / df.Product.value_counts().sum()) * 100
plt.pie(percentages, labels=df.Product.value_counts().head(3).index, autopct='%1.2f%%')
plt.title("Top 3 Products (Percentage)")  
plt.show()

Observaiton: The top 3 products of adidas are shown mens athletic footwear, mens street footwear and womens apparel.
# In[188]:


import warnings
warnings.filterwarnings("ignore")

# bar chart - Total sales each year
df.loc[:, 'Invoice Date'] = pd.to_datetime(df['Invoice Date'])

# Extract year from 'Invoice Date'
df['Year'] = df['Invoice Date'].dt.year

# Calculate total sales per year
yearly_sales = df.groupby('Year')['Units Sold'].sum()

# Create bar chart
plt.figure(figsize=(8, 6))
yearly_sales.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Total Units Sold')
plt.title('Total Units Sold by Year')
plt.xticks(rotation=0)
plt.show()

observation: sales has significantly increased in 2021 than 2020
# In[158]:


# Bar chart- Top 5 retailers
    df = df.groupby('Retailer')['Units Sold'].sum().reset_index()
    top_5_retailers = df.sort_values(by='Units Sold', ascending=False).head(5)
    retailer_names = top_5_retailers['Retailer'].to_numpy()
    units_sold = top_5_retailers['Units Sold'].to_numpy()
 
    plt.bar(retailer_names, units_sold)
    plt.xlabel('Retailer')
    plt.ylabel('Units Sold')
    plt.title('Top 5 Retailers by Units Sold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

Onservation: west gear and footlocker outlets sold the most products
# In[186]:


#Bar chart- sales methods
sales_by_method = df.groupby('Sales Method')['Units Sold'].sum()

# Get positions for each sales method (categorical data needs specific positioning)
sales_method_positions = range(len(sales_by_method))  # Create positions 0, 1, 2, ...

# Create bar chart
plt.figure(figsize=(6, 4))
plt.bar(sales_method_positions, sales_by_method)  # Use positions for x-axis
plt.xlabel('Sales Method')
plt.ylabel('Total Units Sold')
plt.title('Total Units Sold by Sales Method')
plt.xticks(sales_method_positions, sales_by_method.index, rotation=0)  # Set x-axis labels with positions
plt.show()

observation: Most sales were made through online 