#!/usr/bin/env python
# coding: utf-8

# ## Starting with Data

# In[8]:


import pandas as pd
surveys_df = pd.read_csv("surveys.csv")


# In[10]:


surveys_df


# In[11]:


surveys_df.head() 


# In[12]:


type(surveys_df)


# In[13]:


surveys_df.dtypes


# In[19]:


# Using our DataFrame surveys_df, try out the attributes & methods below to see what they return.

# surveys_df.columns
# surveys_df.shape Take note of the output of shape - what format does it return the shape of the DataFrame in?

# HINT: More on tuples, here.

# surveys_df.head() Also, what does surveys_df.head(15) do?
# surveys_df.tail()

surveys_df.columns


# In[16]:


surveys_df.shape


# In[17]:


surveys_df.head()


# In[18]:


surveys_df.tail()


# In[20]:


pd.unique(surveys_df['species_id'])


# In[21]:


surveys_df['weight'].describe()


# In[24]:


grouped_data = surveys_df.groupby('sex')


# In[25]:


# Summary statistics for all numeric columns by sex
grouped_data.describe()


# In[26]:


# Provide the mean for each numeric column by sex
grouped_data.mean()


# In[30]:


# What happens when you group by two columns using the following syntax and then calculate mean values?
grouped_data2 = surveys_df.groupby(['plot_id', 'sex'])
grouped_data2.mean()


# In[31]:


species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)


# In[32]:


surveys_df.groupby('species_id')['record_id'].count()['DO']


# In[33]:


# Multiply all weight values by 2
surveys_df['weight']*2


# In[34]:


# Make sure figures appear inline in Ipython Notebook
get_ipython().run_line_magic('matplotlib', 'inline')
# Create a quick bar chart
species_counts.plot(kind='bar');


# In[35]:


total_count = surveys_df.groupby('plot_id')['record_id'].nunique()
# Let's plot that too
total_count.plot(kind='bar');


# In[36]:


d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
pd.DataFrame(d)


# In[37]:


# Plot stacked data so columns 'one' and 'two' are stacked
my_df = pd.DataFrame(d)
my_df.plot(kind='bar', stacked=True, title="The title of my graph")


# In[39]:


by_site_sex = surveys_df.groupby(['plot_id', 'sex'])
site_sex_count = by_site_sex['weight'].sum()
spc = site_sex_count.unstack()
s_plot = spc.plot(kind='bar', stacked=True, title="Total weight by site and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Plot")


# ### Indexing, Slicing and Subsetting DataFrames in Python

# In[40]:


# TIP: use the .head() method we saw earlier to make output shorter
# Method 1: select a 'subset' of the data using the column name
surveys_df['species_id']

# Method 2: use the column name as an 'attribute'; gives the same output
surveys_df.species_id


# In[41]:


surveys_species = surveys_df['species_id']


# In[44]:


# Select the species and plot columns from the DataFrame
surveys_df[['species_id', 'plot_id']]

# What happens when you flip the order?
surveys_df[['plot_id', 'species_id']]

# What happens if you ask for a column that doesn't exist?
#surveys_df['species']
# Error


# In[45]:


surveys_df[0:3]
# Select the first 5 rows (rows 0, 1, 2, 3, 4)
surveys_df[:5]

# Select the last element in the list
# (the slice starts at the last element, and ends at the end of the list)
surveys_df[-1:]


# In[46]:


# Using the 'copy() method'
true_copy_surveys_df = surveys_df.copy()

# Using the '=' operator
ref_surveys_df = surveys_df


# In[48]:


# Assign the value `0` to the first three rows of data in the DataFrame
ref_surveys_df[0:3] = 0

# ref_surveys_df was created using the '=' operator
ref_surveys_df.head()

# true_copy_surveys_df was created using the copy() function
true_copy_surveys_df.head()

# surveys_df is the original dataframe
surveys_df.head()


# ### Slicing Subsets of Rows and Columns in Python

# In[53]:


# iloc[row slicing, column slicing]
surveys_df.iloc[0:3, 1:4]


# In[54]:


surveys_df[surveys_df.year == 2002]


# In[55]:


surveys_df[surveys_df.year != 2002]


# In[56]:


surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]


# In[57]:


pd.isnull(surveys_df)


# In[58]:


# To select just the rows with NaN values, we can use the 'any()' method
surveys_df[pd.isnull(surveys_df).any(axis=1)]


# In[59]:


empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']
print(empty_weights)


# ### Data Types & Format

# In[61]:


# Make sure pandas is loaded
import pandas as pd

# Note that pd.read_csv is used because we imported pandas as pd
surveys_df = pd.read_csv("surveys.csv")


# In[62]:


type(surveys_df)


# In[63]:


surveys_df['sex'].dtype


# In[64]:


surveys_df['record_id'].dtype


# In[65]:


surveys_df.dtypes


# In[66]:


print(5+5)


# In[67]:


print(24-4)


# In[68]:


print(5/9)


# In[69]:


print(10/3)


# In[70]:


# Convert a to an integer
a = 7.83
int(a)


# In[71]:


# Convert b to a float
b = 7
float(b)


# In[72]:


# Convert the record_id field from an integer to a float
surveys_df['record_id'] = surveys_df['record_id'].astype('float64')
surveys_df['record_id'].dtype


# In[74]:


surveys_df['plot_id'].astype("float")


# In[75]:


surveys_df['weight'].mean()


# In[76]:


len(surveys_df[surveys_df['weight'].isna()])
# How many rows have weight values?
len(surveys_df[surveys_df['weight'] > 0])


# In[77]:


df1 = surveys_df.copy()
# Fill all NaN values with 0
df1['weight'] = df1['weight'].fillna(0)


# In[78]:


df1['weight'].mean()


# In[79]:


df1['weight'] = surveys_df['weight'].fillna(surveys_df['weight'].mean())


# In[80]:


df_na = surveys_df.dropna()


# In[82]:


# Write DataFrame to CSV
df_na.to_csv('surveys_complete.csv', index=False)


# ### Combining DataFrames with Pandas

# In[83]:


import pandas as pd
surveys_df = pd.read_csv("surveys.csv",
                         keep_default_na=False, na_values=[""])
surveys_df


# In[86]:


# Read in first 10 lines of surveys table
survey_sub = surveys_df.head(10)

# Grab the last 10 rows
survey_sub_last10 = surveys_df.tail(10)

# Reset the index values to the second dataframe appends properly
survey_sub_last10 = survey_sub_last10.reset_index(drop=True)
# drop=True option avoids adding new index column with old index values

# Stack the DataFrames on top of each other
vertical_stack = pd.concat([survey_sub, survey_sub_last10], axis=0)

# Place the DataFrames side by side
horizontal_stack = pd.concat([survey_sub, survey_sub_last10], axis=1)


# In[88]:


# Write DataFrame to CSV
vertical_stack.to_csv('out.csv', index=False)


# In[89]:


# For kicks read our output back into Python and make sure all looks good
new_output = pd.read_csv('out.csv', keep_default_na=False, na_values=[""])


# ### Joining Two DataFrames

# In[ ]:


# Read in first 10 lines of surveys table
survey_sub = surveys_df.head(10)

# Import a small subset of the species data designed for this part of the lesson.
# It is stored in the data folder.
species_sub = pd.read_csv('data/speciesSubset.csv', keep_default_na=False, na_values=[""])

