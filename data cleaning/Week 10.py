#!/usr/bin/env python
# coding: utf-8

# ## Week 10 Exercise

# In[1]:


3 + 5 * 4


# In[2]:


weight_kg = 60.3
patient_id = '001'
weight_lb = 2.2 * weight_kg
patient_id = 'inflam_' + patient_id
print(weight_lb)
print(patient_id)


# In[3]:


print(patient_id, 'weight in kilograms:', weight_kg)
print(type(60.3))
print(type(patient_id))


# ### Loading Data into Python

# In[4]:


import numpy


# In[5]:


numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')


# In[6]:


data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')


# In[12]:


print(data)


# In[8]:


print(type(data))


# In[9]:


print(data.shape)


# In[10]:


print('first value in data:', data[0, 0])


# In[11]:


print('middle value in data:', data[29, 19])


# ### Slicing Data

# In[13]:


print(data[0:4, 0:10])


# In[14]:


print(data[5:10, 0:10])


# In[15]:


small = data[:3, 36:]
print('small is:')
print(small)


# ### Analyzing data

# In[16]:


print(numpy.mean(data))


# In[17]:


maxval, minval, stdval = numpy.amax(data), numpy.amin(data), numpy.std(data)

print('maximum inflammation:', maxval)
print('minimum inflammation:', minval)
print('standard deviation:', stdval)


# In[18]:


patient_0 = data[0, :] # 0 on the first axis (rows), everything on the second (columns)
print('maximum inflammation for patient 0:', numpy.amax(patient_0))


# In[19]:


print('maximum inflammation for patient 2:', numpy.amax(data[2, :]))


# In[20]:


print(numpy.mean(data, axis=0))


# In[21]:


print(numpy.mean(data, axis=0).shape)


# In[22]:


print(numpy.mean(data, axis=1))


# In[23]:


element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])


# In[25]:


#What is the value of element[:4]? What about element[4:]? Or element[:]?

print('elements from 0 to 4: ', element[0:4])
print('elements from 4 till end: ', element[4:])
print('elements from the start till end: ', element[:])


# In[26]:


#What is element[-1]? What is element[-2]?

print('last element:', element[-1])
print('last second element:', element[-2])


# In[27]:


#How can we rewrite the slice for getting the last three characters of element, 
#so that it works even if we assign a different string to element? 
#Test your solution with the following strings: carpentry, clone, hi.

element = 'oxygen'
print('last three characters:', element[-3:])
element = 'carpentry'
print('last three characters:', element[-3:])
element = 'clone'
print('last three characters:', element[-3:])
element = 'hi'
print('last three characters:', element[-3:])


# In[29]:


#The expression element[3:3] produces an empty string, i.e., a string that contains no characters. If data holds our array of patient data, what does data[3:3, 4:4] produce? What about data[3:3, :]?

print('output for ', data[3:3, 4:4])
print('output for ', data[3:3, :])


# In[30]:


import numpy

A = numpy.array([[1,2,3], [4,5,6], [7, 8, 9]])
print('A = ')
print(A)

B = numpy.hstack([A, A])
print('B = ')
print(B)

C = numpy.vstack([A, A])
print('C = ')
print(C)


# ### Change in Inflammation

# In[31]:


patient3_week1 = data[3, :7]
print(patient3_week1)


# In[32]:


[ 0 - 0, 2 - 0, 0 - 2, 4 - 0, 2 - 4, 2 - 2 ]


# In[33]:


numpy.diff(patient3_week1)


# ### Visualizing Data

# In[34]:


import matplotlib.pyplot
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()


# In[35]:


ave_inflammation = numpy.mean(data, axis=0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()


# In[36]:


max_plot = matplotlib.pyplot.plot(numpy.amax(data, axis=0))
matplotlib.pyplot.show()


# In[37]:


min_plot = matplotlib.pyplot.plot(numpy.amin(data, axis=0))
matplotlib.pyplot.show()


# In[38]:


import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.amax(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.amin(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig('inflammation.png')
matplotlib.pyplot.show()


# #### Plot Scaling

# In[40]:


import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.amax(data, axis=0))

min_data = numpy.amin(data, axis=0)
axes3.set_ylabel('min')
axes3.plot(min_data)
axes3.set_ylim(numpy.amin(min_data), numpy.amax(min_data) * 1.1)

fig.tight_layout()

matplotlib.pyplot.savefig('inflammation.png')
matplotlib.pyplot.show()


# ##### Using drawstyle to avoid interpolation between the points and instead making a pattern with steps

# In[41]:


import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0), drawstyle='steps-mid')

axes2.set_ylabel('max')
axes2.plot(numpy.amax(data, axis=0), drawstyle='steps-mid')

axes3.set_ylabel('min')
axes3.plot(numpy.amin(data, axis=0), drawstyle='steps-mid')

fig.tight_layout()

matplotlib.pyplot.show()


# #### Creating a plot to show the standard deviation (numpy.std) of the inflammation data for each day across all patients.

# In[42]:


std_plot = matplotlib.pyplot.plot(numpy.std(data, axis=0))
matplotlib.pyplot.show()


# #### Changing the orientation of plots

# In[44]:


import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

# change figsize (swap width and height)
fig = matplotlib.pyplot.figure(figsize=(3.0, 10.0))

# change add_subplot (swap first two parameters)
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.amax(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.amin(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()


# ### Storing Multiple Values In Lists

# #### Python Lists

# In[45]:


odds = [1, 3, 5, 7]
print('odds are:', odds)


# In[46]:


print('first element:', odds[0])
print('last element:', odds[3])
print('"-1" element:', odds[-1])


# In[49]:


names = ['Curie', 'Darwing', 'Turing']  # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin'  # correct the name
print('final value of names:', names)


# In[50]:


name = 'Darwin'
name[0] = 'd'


# In[51]:


mild_salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
hot_salsa = mild_salsa        # <-- mild_salsa and hot_salsa point to the *same* list data in memory
hot_salsa[0] = 'hot peppers'
print('Ingredients in mild salsa:', mild_salsa)
print('Ingredients in hot salsa:', hot_salsa)


# In[52]:


mild_salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
hot_salsa = list(mild_salsa)        # <-- makes a *copy* of the list
hot_salsa[0] = 'hot peppers'
print('Ingredients in mild salsa:', mild_salsa)
print('Ingredients in hot salsa:', hot_salsa)


# ### Nested Lists

# In[63]:


veg = [['lettuce', 'lettuce', 'peppers', 'zucchini'],
     ['lettuce', 'lettuce', 'peppers', 'zucchini'],
     ['lettuce', 'cilantro', 'peppers', 'zucchini']]

print('Print 3rd array in the list: ',veg[2])
print('Print 1st array in the list: ',veg[0])
print('Print 1st element in the first array of the list: ',veg[0][0])
print('Print 2nd element in the thrid array of the list: ',veg[1][2])
sample_ages = [10, 12.5, 'Unknown']
odds.append(11)
print('odds after adding a value:', odds)

#Pop elements from the list
removed_element = odds.pop(0)
print('odds after removing the first element:', odds)
print('removed_element:', removed_element)

# Reverse List
odds.reverse()
print('odds after reversing:', odds)


odds = [3, 5, 7]
primes = odds
primes.append(2)
print('primes:', primes)
print('odds:', odds)

# If we use we list it won't be able to modify or append the list
odds = [3, 5, 7]
primes = list(odds)
primes.append(2)
print('primes:', primes)
print('odds:', odds)


# Subsets of lists and strings can be accessed by specifying ranges of values in brackets
binomial_name = 'Drosophila melanogaster'
group = binomial_name[0:10]
print('group:', group)

species = binomial_name[11:23]
print('species:', species)

chromosomes = ['X', 'Y', '2', '3', '4']
autosomes = chromosomes[2:5]
print('autosomes:', autosomes)

last = chromosomes[-1]
print('last:', last)


# ### Slicing Lists

# In[65]:


string_for_slicing = 'Observation date: 02-Feb-2013'
list_for_slicing = [['fluorine', 'F'],
                    ['chlorine', 'Cl'],
                    ['bromine', 'Br'],
                    ['iodine', 'I'],
                    ['astatine', 'At']]


# Non-continuous slices
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print('subset', subset)

# If you want to take a slice from the beginning of a sequence, you can omit the first index in the range:
date = 'Monday 4 January 2016'
day = date[0:6]
print('Using 0 to begin range:', day)
day = date[:6]
print('Omitting beginning index:', day)

#And similarly, you can omit the ending index in the range to take a slice to the very end of the sequence:
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
sond = months[8:12]
print('With known last position:', sond)
sond = months[8:len(months)]
print('Using len() to get last entry:', sond)
sond = months[8:]
print('Omitting ending index:', sond)


# #### Printing elements in the list with a loop

# In[67]:


# without loop
odds = [1, 3, 5, 7]
print(odds[0])
print(odds[1])
print(odds[2])
print(odds[3])



# In[68]:


# If we access elements outside the size of the array
odds = [1, 3, 5]
print(odds[0])
print(odds[1])
print(odds[2])
print(odds[3])


# In[69]:


# Using loop
odds = [1, 3, 5, 7]
for num in odds:
    print(num)
    

name = 'Rosalind'
for name in ['Curie', 'Darwin', 'Turing']:
    print(name)
print('after the loop, name is', name)


# In[70]:


# Write a loop that calculates the same result as 5 ** 3 using multiplication
result = 1
for number in range(0, 3):
    result = result * 5
print(result)


#Write a loop that calculates the sum of elements in a list by adding each element and printing the final value, so [124, 402, 36] prints 562
numbers = [124, 402, 36]
summed = 0
for num in numbers:
    summed = summed + num
print(summed)


# ### Analyzing data from multiple files

# In[72]:


import glob
print(glob.glob('inflammation*.csv'))


# In[74]:


import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('inflammation*.csv'))
filenames = filenames[0:4]
for filename in filenames:
    print(filename)

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.amax(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.amin(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()


# ### Plotting differences

# In[75]:


import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('inflammation*.csv'))

data0 = numpy.loadtxt(fname=filenames[0], delimiter=',')
data1 = numpy.loadtxt(fname=filenames[1], delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

matplotlib.pyplot.ylabel('Difference in average')
matplotlib.pyplot.plot(numpy.mean(data0, axis=0) - numpy.mean(data1, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()


# ### Generate Composite Statistics

# In[77]:


import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('inflammation*.csv')
composite_data = numpy.zeros((60,40))

for filename in filenames:
    data = numpy.loadtxt(fname = filename, delimiter=',')
    composite_data = composite_data + data

composite_data = composite_data / len(filenames)

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(composite_data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.amax(composite_data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.amin(composite_data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()

