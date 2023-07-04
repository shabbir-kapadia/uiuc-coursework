#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


netflix = pd.read_csv('netflix_titles.csv')


# In[3]:


data = netflix.copy()


# In[4]:


netflix.shape


# In[5]:


netflix.head()


# In[6]:


netflix.info()


# In[7]:


netflix.isna().sum()


# In[8]:


for i in netflix.columns:
  na=netflix[i].isna().sum()
  percent=na/len(netflix)*100


# In[9]:


netflix = netflix.dropna(subset=['cast','country','date_added','rating','duration'],how='any')


# In[10]:


netflix['director'] = netflix['director'].fillna(value='Not Found')


# In[11]:


netflix.isna().sum()


# In[12]:


netflix.drop('description',axis=1,inplace=True)


# In[13]:


netflix.date_added = pd.to_datetime(netflix.date_added)


# In[14]:


def split_data(col1,col2):
    data1 = data[col1].str.split(',',expand=False)
    data2 = data[col2].squeeze()
    df = pd.concat([data1,data2],axis=1).explode(col1).reset_index(drop=True)   
    df[col1] = df[col1].str.strip()
    return df.value_counts().reset_index()


# In[15]:


df1 = split_data('country','type').rename(columns={ 0 :"count"})
df2 = split_data('listed_in','type').rename(columns={ 0 :"count"})


# In[16]:


df1


# In[17]:


df2


# In[18]:


df3 = netflix.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(df3, values='counts', names='rating',
title='Distribution of Content Ratings on Netflix')
pieChart.show()


# In[19]:


df3


# In[20]:


netflix['cast']=netflix['cast'].fillna('No Cast Specified')
filtered_cast=pd.DataFrame()
filtered_cast=netflix['cast'].str.split(',',expand=True).stack()
filtered_cast=filtered_cast.to_frame()
filtered_cast.columns=['Actor']
actors=filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content')
actors=actors[actors.Actor !='No Cast Specified']
actors=actors.sort_values(by=['Total Content'],ascending=False)
actorsTop5=actors.head()
actorsTop5=actorsTop5.sort_values(by=['Total Content'])
actorsTop5


# In[21]:


temp = list()
clean_data = data.dropna()
clean_data.reset_index(inplace=True)
for ind, element in clean_data.iterrows():
    type_show = element['type']
    for director in str(element['director']).split(','):
        temp.append([type_show, director])
director_data = pd.DataFrame(temp, columns= ['type', 'director'])
director_data


# In[22]:


director_data_count = director_data.value_counts().to_frame()
director_data_count.reset_index(level=[0,1], inplace=True)
famous_director = director_data_count.rename(columns={0:'count'})
famous_director


# In[23]:


for unique_type in famous_director['type'].unique():
    bar, ax = plt.subplots(figsize=(10,10))
    sns.barplot(x = 'director', y = 'count', data = famous_director[famous_director['type'] == unique_type].iloc[:5])
    plt.xlabel('Director in {}'.format(str(unique_type)))
    plt.ylabel('Frequency')
    plt.title('Famous Director in {}'.format(str(unique_type)), size=20)


# In[24]:


movie_data = netflix[netflix['type'] == 'Movie']
tv_show_data = netflix[netflix['type'] == 'TV Show']
# bar,ax = plt.subplots(1,2,figsize=(10,10))
temp = netflix[['type', 'release_year']]
temp = temp.value_counts().to_frame()
temp.reset_index(level=[0,1], inplace=True)
temp = temp.rename(columns = {0:'count'})
temp = pd.concat([temp[temp['type'] == 'Movie'][:5], temp[temp['type']== 'TV Show'][:5]])


# In[25]:


# ax, bar = plt.subplots(figsize = (10,10))
sns.catplot(x = 'release_year', y = 'count', hue = 'type', data = temp, kind = 'point')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.title('Growth of Movie/TV Show over Years', size=14)


# In[26]:


df4=netflix[['type','release_year']]
df4=df4.rename(columns={"release_year": "Release Year"})
df5=df4.groupby(['Release Year','type']).size().reset_index(name='Total Content')
df5=df5[df5['Release Year']>=2010]
df5


# In[27]:


df4=netflix[['type','release_year']]
df4=df4.rename(columns={"release_year": "Release Year"})
df5=df4.groupby(['Release Year','type']).size().reset_index(name='Total Content')
df5=df5[df5['Release Year']>=2010]
fig3 = px.line(df5, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the year')
fig3.show()


# In[ ]:




