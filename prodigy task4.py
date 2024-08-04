#!/usr/bin/env python
# coding: utf-8

# # Aim: Analyze and visualize sentiment patterns in social media data to understand public opinion and attibutes towards specific topics or brands

# In[6]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


plt.style.use('ggplot')


# In[8]:


pip install nltk


# In[9]:


import nltk


# In[10]:


df = pd.read_csv(r'D:\hp\Documents\JAIN SEM 6\SMA\lab\archive 2\Musical_instruments_reviews.csv')


# In[11]:


print(df)


# In[12]:


df.head()


# In[13]:


ax = df['overall'].value_counts().sort_index()     .plot(kind = "bar" , 
     title = 'count of reviews by stars' , 
     figsize=(10,5))
ax.set_xlabel('Review stars')
plt.show() 


# In[14]:


##basic NLTK


# In[18]:


example = df['reviewText'][1000]
print(example)


# In[19]:


tokens= nltk.word_tokenize(example)
tokens[:10]


# In[20]:


tagged= nltk.pos_tag(tokens)
tagged[:10]


# In[15]:


entities = nltk.chunk.ne_chunk(tagged)
entities.pprint()


# # VADER sentiment scoring

# In[21]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()


# In[22]:


sia


# In[23]:


sia.polarity_scores("This guitar was absolutely fantastic!")


# In[24]:


sia.polarity_scores("this violin is the worst ")


# In[25]:


sia.polarity_scores(example)


# In[38]:


#Run the polarity score on the entire dataset
df
    


# In[39]:


res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = str(row['reviewText'])
    myid = row['reviewerID']
    res[myid]= sia.polarity_scores(text)


# In[40]:


res


# In[41]:


vaders = pd.DataFrame(res).T
vaders = vaders.reset_index().rename(columns={'index': 'reviewerID'})
vaders = vaders.merge(df, how='left')


# In[42]:


#sentiment score and metadata
vaders.head()


# In[69]:


##Plot VADER results


# In[43]:


ax = sns.barplot(data=vaders, x='overall', y= 'compound')
ax.set_title("compund score by amazon review")
plt.show()


# In[80]:


fig, axs = plt.subplots(1, 3, figsize=(15,3))
sns.barplot(data=vaders, x='overall', y= 'pos', ax=axs[0])
sns.barplot(data=vaders, x='overall', y= 'neu', ax=axs[1])
sns.barplot(data=vaders, x='overall', y= 'neg', ax=axs[2])
axs[0].set_title('positive')
axs[1].set_title('Nuetral')
axs[2].set_title('negative')
plt.show()


# In[ ]:




