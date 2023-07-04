#!/usr/bin/env python
# coding: utf-8

# ### Week 11 Exercise

# ### Writing loops and conditions

# In[1]:


num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')


# In[2]:


# Conditions without else
num = 53
print('before conditional...')
if num > 100:
    print(num, 'is greater than 100')
print('...after conditional')

# Multiple if-else statements
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is negative')
    
# Using and & or keywords to run specific cases
if (1 > 0) and (-1 >= 0):
    print('both parts are true')
else:
    print('at least one part is false')


# ### Using Inflammation dataset to perform these operations

# In[5]:


import numpy

# Implementing the if case
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

max_inflammation_0 = numpy.amax(data, axis=0)[0]
max_inflammation_20 = numpy.amax(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.amin(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
    
    
#Impleneting the elif case
data = numpy.loadtxt(fname='inflammation-03.csv', delimiter=',')

max_inflammation_0 = numpy.amax(data, axis=0)[0]
max_inflammation_20 = numpy.amax(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.amin(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')


# In[7]:


# To check which case gets executed in the nested if conditions. In this case C will be printed as 4 < 5
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')

# In place multiplication and addition
x = 1  # original value
x += 1 # add one to x, assigning result back to x
x *= 3 # multiply x by 3
print(x)


# In[8]:


#Write some code that sums the positive and negative numbers in a list separately, using in-place operators. Do you think the result is more or less readable than writing the same without in-place operators?
positive_sum = 0
negative_sum = 0
test_list = [3, 4, 6, 1, -1, -5, 0, 7, -8]
for num in test_list:
    if num > 0:
        positive_sum += num
    elif num == 0:
        pass
    else:
        negative_sum += num
print(positive_sum, negative_sum)


# In[9]:


# Write a loop that counts the number of vowels in a character string.
#Test it on a few individual words and full sentences.
#Once you are done, compare your solution to your neighbor’s. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?

vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print('The number of vowels in this string is ' + str(count))


# ### Creating functions

# In[24]:


# This function is to convert celsius to Kelvin

def celsius_to_kelvin(temp_c):
    return temp_c + 273.15
    
    # This function is to convert fahrenheit to Kelvin
    def fahr_to_kelvin(temp_f):
        temp_c = fahr_to_celsius(temp_f)
        temp_k = celsius_to_kelvin(temp_c)
    return temp_k

    print('boiling point of water in Kelvin:', fahr_to_kelvin(212.0))

print('freezing point of water in Kelvin:', celsius_to_kelvin(0.))


# 
# ### Creating function for Inflammation Dataset

# In[25]:


import glob
import numpy
import matplotlib.pyplot
def visualize(filename):

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

def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.amax(data, axis=0)[0] == 0 and numpy.amax(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.amin(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')

        
filenames = sorted(glob.glob('inflammation*.csv'))

for filename in filenames[:3]:
    print(filename)
    visualize(filename)
    detect_problems(filename)


# ### Testing and documenting

# In[29]:


def offset_mean(data, target_mean_value):
    return (data - numpy.mean(data)) + target_mean_value
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(offset_mean(data, 0))

print('original min, mean, and max are:', numpy.amin(data), numpy.mean(data), numpy.amax(data))
offset_data = offset_mean(data, 0)
print('min, mean, and max of offset data are:',
      numpy.amin(offset_data),
      numpy.mean(offset_data),
      numpy.amax(offset_data))


# In[30]:


def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return numpy.sqrt(d / (len(p) - 1))

def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))


# In[31]:


#“Adding” two strings produces their concatenation: 'a' + 'b' is 'ab'. Write a function called fence that takes two parameters called original and wrapper and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:
def fence(original, wrapper):
    return wrapper + original + wrapper
result = fence('hello', '*')
print(result)  # Output: *hello*


# In[37]:


#Q2 What is the output of this function?
def add(a, b):
    print(a + b)
A = add(7, 3)
print(A)

#Q3 Print hm as output
def outer(a):
    return a[0] + a[-1]
print(outer('helium'))

#Q4 Rescaling an array
def rescale(input_array):
    L = numpy.amin(input_array)
    H = numpy.amax(input_array)
    output_array = (input_array - L) / (H - L)
    return output_array
print(rescale([1,2,3,4,5,6]))


# ### Syntax Errors

# In[39]:


def another_function():
    print('Syntax errors are annoying.')
    print('But at least Python tells us about them!')
    print('So they are usually not too hard to fix.')

another_function()


# In[40]:


#Identifying variable name errors
message = ''
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + 'a'
    else:
        message = message + 'b'
print(message)


# In[41]:


#Identifying index errors
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[-1])


# #### Defensive Programming

# In[44]:


def get_total(values):
    assert len(values) > 0
    for element in values:
        assert int(element)
    values = [int(element) for element in values]
    total = sum(values)
    assert total > 0
    return total
#The first assertion checks that the input sequence values is not empty. An empty sequence such as [] will make it fail.
#The second assertion checks that each value in the list can be turned into an integer. Input such as [1, 2, 'c', 3] will make it fail.
#The third assertion checks that the total of the list is greater than 0. Input such as [-10, 2, 3] will make it fail.


# ### Debugging

# In[45]:


patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is:", bmi)

#Bugs Found
#1 .The loop is not being utilised correctly. height and weight are always set as the first patient’s data during each iteration of the loop.

#2. The height/weight variables are reversed in the function call to calculate_bmi(...), the correct BMIs are 21.604938, 22.160665 and 51.903114.


# ### Command Line Arguments

# In[50]:


import sys
print('version is', sys.version)
print('sys.argv is', sys.argv)

