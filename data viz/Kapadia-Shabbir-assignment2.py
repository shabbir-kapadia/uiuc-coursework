#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("building_inventory.csv")


# In[4]:


df = pd.read_csv("building_inventory.csv", na_values = {
    "Year Acquired":0,
    "Year Constructed":0,
    "Congress Dist":0
})


# In[5]:


plt.rcParams["figure.dpi"] = 130
plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')
#plt.style.use('bmh')


# # Relationship between the year acquired and the year constructed

# In[6]:


plt.plot(df["Year Acquired"],df["Year Constructed"],'.')
plt.xlabel("Year Acquired")
plt.ylabel("Year Constructed")
plt.title("Relationship between the year acquired and the year constructed")


# All the Na values for the Year Acquired and Year Constructed were filtered out as these cannot contain null values.
# 
# The relation between the year acquired and the year constructed is quite clear from the above plotted scatter plot. There is a linear relationship between both the given entities which is one of the successes.
# 
# One of the very evident shortcoming is that all the points have overlapped which becomes very difficult to understand from a user perspective.
# 

# # Total square footage as a function of congressional district

# In[7]:


df["Congress Dist"]


# In[8]:


df["Square Footage"]


# In[9]:


df_by_cong_dist = pd.DataFrame(df.groupby("Congress Dist").sum()["Square Footage"])
df_by_cong_dist.reset_index(inplace=True)
df_by_cong_dist


# In[10]:


plt.bar(df_by_cong_dist["Congress Dist"],df_by_cong_dist["Square Footage"])
plt.xticks(ticks=np.linspace(1,18,18))
plt.ylabel("Square Footage")
plt.xlabel("Congress Dist")
plt.title("Total square footage as a function of congressional district")


# In the above question we have to find out Total square footage as a function of congressional district so I have firstly created a data frame of Congress Dist by doing a group by and using the sum function to get the sum of all the data by using the below given command.
# df_by_cong_dist = pd.DataFrame(df.groupby("Congress Dist").sum()["Square Footage"])
# 
# By using the reset_index command I have converted the original index to a column which is displayed in the above given output. After that, I have created a simple bar graph to display all the congress dist from 1 to 18 against the square footage.
# 
# One of the shortcomings in this approach is that the X-axis has some values to be displayed close to null but it is not actually null and has some value associated with it. For example, number 9 is not 0 but it seems through the graph that it is null.
# 

# # Average square footage per floor as a function of congressional district

# In[11]:


df_by_cong_dist_avg = pd.DataFrame(df.groupby("Congress Dist").sum())
df_by_cong_dist_avg.reset_index(inplace=True)
df_by_cong_dist_avg


# In[12]:


df_by_cong_dist_avg["Avg SqFootage Per Floor"] = df_by_cong_dist_avg["Square Footage"]/df_by_cong_dist_avg["Total Floors"]


# In[13]:


df_by_cong_dist_avg.head()


# In[14]:


plt.bar(df_by_cong_dist_avg["Congress Dist"],df_by_cong_dist_avg["Avg SqFootage Per Floor"])
plt.xticks(ticks=np.linspace(1,18,18))
plt.ylabel("Avg Sq Footage Per Floor")
plt.xlabel("Congress Dist")
plt.title("Average square footage per floor as a function of congressional district")


# The approach used for the above question was to first find out the average square footage per floor which was done by dividing the square footage by the total number of floors in the building to get the average square footage per floor.
# 
# The data obtained was then simply plot using a graph plot putting Congress Dist on the X axis and putting Avg Sq footage on the Y axis.
# 
# One of the shorcomings in this approach is that the data being displayed on the graph does not have the data mentioned properly and the user has to guess the value based on the grids that have been made.
# 
# All in all the visualization makes it very clear about the average sq footage per floor for all the different 18 congress districts.

# # Square footage for the five most common departments as a function of year

# In[15]:


df["Agency Name"].value_counts(sort=True)


# In[16]:


df_by_agency_name = pd.DataFrame(df.groupby(["Agency Name","Year Constructed"]).sum()["Square Footage"])
df_by_agency_name.reset_index(inplace=True)
df_by_agency_name


# In[17]:


df["Agency Name"].value_counts(sort=True)
most_cmn_dept = list(df["Agency Name"].value_counts(sort=True).keys()[0:5])
most_cmn_dept


# In[18]:


for x in most_cmn_dept:
    df_each = df_by_agency_name[df_by_agency_name['Agency Name'] == x]
    plt.figure(figsize=(10,6))
    sq_min = df_each["Square Footage"].min()
    sq_max = df_each["Square Footage"].max()
    plt.yticks(ticks=np.linspace(sq_min,sq_max,12))
    plt.scatter(df_each["Year Constructed"],df_each["Square Footage"])
    plt.title("Square Footage vs Year Constructed for The " +x)
    plt.ticklabel_format(style='plain')
    plt.xlabel("Year Constructed")
    plt.ylabel("Square Footage")


# By applying value counts on the main data frame we were able to obtain the top 5 most popular departments in the university.
# 
# We then created a new data frame by applying group by to Agency Name and Year constructed. After that by applying reset index we converted the index to a column which can be used further for processing.
# 
# Finally, the most common departments were checked in the data frame and a scatter plot was created based on the data that we had for processing.
# 
# Also, every year has only one value associated with it. But through the scatter plot it becomes very difficult to identify the values on the lower side. The area constructed per year cannot be easily identified as there is overlapping of the dots on the scale.
