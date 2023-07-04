#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


import json
import cartopy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing


# In[2]:


with open("Earth Meteorite Landings.json") as f:
    data = json.load(f)


# In[3]:


# print(json.dumps(data, indent=2))


# In[4]:


data[0]


# In[5]:


df = pd.DataFrame(data)
df = df.drop([":@computed_region_cbhk_fwbd", ":@computed_region_nnqa_25f4"], axis=1)
df = df.astype(str)


# In[6]:


# df['mass']
df.mass.value_counts()


# In[7]:


new_df = df.drop(df[df.mass == 'nan'].index)
new_df['year'] = new_df['year'].astype(str)
new_df = new_df.drop(new_df[new_df.year == '<NA>'].index)
# new_df.mass.value_counts()
new_df["mass"] = np.floor(pd.to_numeric(new_df["mass"], errors='coerce')).astype('Int64')
# new_df = new_df[new_df["mass"] > 500000]
# new_df.mass.value_counts()

new_df['year'] = pd.to_datetime(df['year'], errors = 'coerce')
new_df['year'] = new_df['year'].dt.year.astype('Int64')
new_df


# In[8]:


amounts_by_year_top_five_df = new_df.year.value_counts().rename_axis('year').reset_index(name='counts')
amounts_by_year_top_five_df = amounts_by_year_top_five_df.nlargest(5, 'counts', keep='first')
amounts_by_year_top_five_df = amounts_by_year_top_five_df.set_index('year')
amounts_by_year_top_five_df = amounts_by_year_top_five_df.sort_values(by=['year'])
amounts_by_year_top_five_df['counts'].plot(kind='bar', grid=True, figsize=(10,5), ylim=(5, 20), title='Amounts of meteorites (top five)')


# In[9]:


new_df['amounts_by_year'] = new_df.groupby(['year'])['year'].transform('count').astype('Int64')
new_df = new_df.dropna()
new_df


# In[10]:


mass_top_five_df = mass_year_df.nlargest(5, 'mass', keep='all')
mass_top_five_df = mass_top_five_df.sort_values(by=['year'])
mass_top_five_df['mass'].plot(kind='bar', grid=True, figsize=(10,5), ylim=(40000, 25000000), title='Mass of meteorites (top five)')


# In[ ]:


lat = []
lon = []
for i in range(len(new_df['reclat'])):
    try:
        lat.append(new_df['reclat'][i])
        lon.append(new_df['reclong'][i])
    except:
        continue


# In[ ]:


fig = plt.figure(dpi=300)
ax = fig.add_subplot(111, projection=cartopy.crs.PlateCarree())
ax.scatter([lon], [lat], s=0.5, color="red")
ax.coastlines()
ax.set_title('Earth Meteorite Landings', fontsize=8)
ax.set_global()


# In[ ]:


fig = plt.figure(figsize=(25,12))
ax = fig.add_subplot(1,1,1, projection=cartopy.crs.PlateCarree())
ax.stock_img()
plt.scatter(x=[lon], y=[lat],
            color="brown",
            s=10,
            alpha=1,
            transform=cartopy.crs.PlateCarree())

ax.add_feature(cartopy.feature.COASTLINE, edgecolor="dodgerblue")
ax.add_feature(cartopy.feature.BORDERS, edgecolor="green")

ax.set_title('Earth Meteorite Landings', fontsize=30)
ax.set_global()


plt.show()


# # 1. Distribution of Meteorite by reclass

# In[47]:


diff_rec = new_df['recclass'].value_counts()
diff_rec[diff_rec > 50].plot.pie(autopct='%.2f',figsize=(6,6))
plt.title('Occurence of Different Types of Meteorite', fontsize=12)


# In[18]:


L6 = new_df[new_df.recclass=='L6']
H5 = new_df[new_df.recclass=='H5']


# In[45]:


plt.figure(figsize=(15,7))

plt.subplot(221)
plt.hist(L6.year.values,bins=np.arange(1900,2014,2),lw=2,histtype='step')
plt.ylabel('L6')
plt.xticks(np.arange(1900,2015,10))

plt.subplot(222)
plt.hist(H5.year.values,bins=np.arange(1900,2014,2),lw=2,histtype='step')
plt.ylabel('H5')
plt.xticks(np.arange(1900,2015,10))
plt.show


# In[54]:


plt.subplot(2)
new_df.year.hist(bins=np.arange(1900,2018,1),figsize=(14,8),histtype='step')
plt.title('Discoveries Per Year')
plt.xlim(1900,2018)

plt.subplot(2)
new_df.year.hist(bins=np.arange(1900,2018,10),figsize=(14,8),histtype='stepfilled')
plt.title('Discoveries Per Decade')
plt.xlim(1900,2018)


# In[ ]:




