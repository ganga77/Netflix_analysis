#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
df = pd.read_csv(r'/Users/gangasingh/Downloads/file.csv')
df


# In[47]:


df.describe()


# In[48]:


df.info()


# In[49]:


# Duplicate Records 
df[df.duplicated()]


# In[50]:


df.drop_duplicates(inplace=True)


# In[51]:


# If null values present?
df.isnull().sum()


# In[52]:


df[df['Title'].isin(['House of Cards'])]


# In[53]:


#which year highest number of tv shows and movies were released
df.info()


# In[54]:


df['Release_Date'] = df['Release_Date'].str.strip()
df['Date_N'] = pd.to_datetime(df['Release_Date'], format='%B %d, %Y')


# In[55]:


df.drop(columns={'Release_Date'})


# In[57]:


df.rename(columns={'Date_N': 'Release-date'}, inplace=True)


# In[70]:


df['year'] = pd.DatetimeIndex(df['Release-date']).year


# In[76]:


#Get counts of movies and tvshows released in years
year_movies = df.groupby(['year']).size()
year_movies


# In[82]:


# How many movies and tvshows are in this dataset

grp = df.groupby(['Category']).Category.count()
grp


# In[103]:


df['year']= pd.DatetimeIndex(df['Release-date']).year


# In[104]:


df


# In[106]:


#movies released in 2020
df[(df['year'] == 2020) & (df['Category']=='Movie')]


# In[107]:


#Show only titles of tv shows which were released in india only
df


# In[111]:


df[(df['Country']=='India') & (df['Category']=='TV Show')]['Title']


# In[118]:


#Show top 10 directors who gave highest number of tv shows and movies

df['Director'].value_counts().head(10)


# In[125]:


#Show all the records where category is movie and type is comedians or country is united kingdom

df[((df['Category']=='Movie') & (df['Type']=='Comedies')) | (df['Country']=='United Kingdom')]


# In[132]:


# in how many movies/tvshows, Tom Cruise was cast
df2 = df.dropna()
df2[df2['Cast'].str.contains('Tom Cruise')]


# In[135]:


# What are the different ratings defined by the netflix

df['Rating'].nunique()


# In[138]:


#How many movies got the 'TV-14' rating in canada?

df[(df['Rating']=='TV-14') & (df['Country']=='Canada') & (df['Category']=='Movie')]


# In[139]:


df.describe()


# In[143]:


df['Duration'] = df['Duration'].astype(str)


# In[144]:


df.info()


# In[149]:


df['Duration']=df['Duration'].str.split().str[0]


# In[150]:


df


# In[151]:


df['Duration'] = df['Duration'].astype(str).astype(int)


# In[154]:


df[df['Duration']==312]


# In[158]:


#which individual country has the highest number of tv shows
df[df['Category']=='TV Show']['Country'].value_counts().head(10)


# In[ ]:




