#!/usr/bin/env python
# coding: utf-8

# # Final Project - Part One (Individual)

# #### In this, I have used the IMDB dataset which I have used to create different types of visualization. 

# In[2]:





# In[120]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 80
plt.style.use('fivethirtyeight')
df = pd.read_csv("divorce.csv")

first = pd.DataFrame(list(zip( df["poor_3544"] , df["mid_3544"], df["rich_3544"] )),
                  index = df["year"] , 
                  columns = [ 'Poor' , 'Mid' , 'Rich' ])
ax = first.plot(title = 'Divorce Rate of people aged 35 - 44', marker = '.', lw=2)
ax.set_xlabel("Year")
ax.set_ylabel("Rate")


second = pd.DataFrame(list(zip( df["poor_4554"] , df["mid_4554"], df["rich_4554"] )),
                  index = df["year"] , 
                  columns = [ 'Poor' , 'Mid' , 'Rich' ])
bx = second.plot(title = 'Divorce Rate of people aged 45 - 54', marker = '.', lw=2, xticks = [1960,1970,1980,1990,2000,2010])
bx.set_xlabel("Year")
bx.set_ylabel("Rate")


# In[118]:





# In[57]:





# In[60]:





# Refined the data by dropping N/A values from it

# In[119]:





# In[13]:





# In[14]:





# In[15]:





# In[16]:





# In[31]:


# plt.plot(df["year"],df["poor_3544"],'-')
# plt.xlabel("year")
# plt.ylabel("Percentage")
# plt.title("Poor people getting divorced over the years")

# df = pd.DataFrame(list(zip( df["poor_3544"])),
#                   index = df["year"] , 
#                   columns = [ 'poor' ])
# df



# ## Top 5 Directors from the Dataset

# By taking the count of the number of the Directors present in the Dataset, I was able to get the Top 5 Directors. I then created a pie chart displaying all the top 5 directors there.

# In[12]:


df.Director.value_counts()[:5].plot.pie(autopct='%.2f',figsize=(8,8))
plt.title('Top 5 Directors')


# ## Top 5 Actors

# Applied the same logic and refined out all the top 5 actors

# In[13]:


df.Actors.value_counts()[:5].plot.pie(autopct='%.2f',figsize=(12,12))
plt.title('Top 5 Actors')


# As the runtime in the dataset was a string and I wanted to use it as an integer. I extracted that runtime and converted it to Integer value by using a regular expression and put that data in a runtime variable.

# In[14]:


runtime = df['Runtime'].str.extract('(\d+)').astype(int)


# In[15]:


df.dtypes


# From the below visualization it becomes quite clear that the data contains values from later 2000s and this data was nowhere available in the late 90s as well. Through this scatter plot it is evident that a lot of movies have had good ratings that is above 6 after the data was available. 

# In[16]:


refined_votes = df[df["imdbRating"] >=0]
refined_years = df[df["Year"] >=0]
plt.plot(refined_years["Year"], refined_votes["imdbRating"],'.')
plt.xlabel("Year")
plt.ylabel("IMDB Rating")


# From the below visualization I have tried to visualise top 5 languages that are being used in the movies. About 83.72% movies are produced in English, while a lot of movies are produced in other languages like Spanish but English is still there as one of the langauges.

# In[17]:


df.Language.value_counts()[:5].plot.pie(autopct='%.2f',figsize=(6,6))
plt.title('Top 5 Languages')


# In[18]:


df["Genre"].value_counts()


# In[21]:


plt.plot(df["Year"],runtime,'.')
plt.yticks(ticks=np.linspace(250,0,10))
plt.xlabel("Year")
plt.ylabel("Runtime")


# In[22]:


runtime


# In the below visualization, I have created a simple histogram with runtimes of all the movies and depicts that a lot of movies produced to take a count approximately 800 movies had runtime of around 100 mins.

# In[24]:


plt.hist(runtime);
plt.xlabel("Runtime");
plt.ylabel("Count");

