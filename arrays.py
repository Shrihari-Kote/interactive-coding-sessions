# The first thing we are going to do is something we've done before
# import a library
# imports are always at the top of the file
import numpy as np # import x as y. x is the library name, y is the shorthand
# When libraries have short names, like math, we don't use a shorthand
import math
import pandas as pd

# If a library is not installed, what do we do? UV!
# In terminal, type: uv add pandas numpy math

# Once you've installed and imported a library, you can access its content using
# the dot notation:
print(math.pi)
print(math.sqrt(9))

# Let's talk about arrays now. Arrays are a new kind of object that live
# inside the numpy package:
my_array = np.array([1,2,3,4,5]) # You create an array by supplying a list
print(my_array)
# It looks a lot like a list
# You can index it
print(my_array[1])
# You can slice it:
print(my_array[0:3])
# So what's the difference between lists and arrays
type(my_array)
# First difference: an array requires that all its elements are of the same type
my_list = ["Quentin",False,42]
type(my_list[0]) # str
type(my_list[1]) # bool

my_array2 = np.array(my_list)
my_array2 # All the elements have been converted to string
# In technical term, we say they were coerced to a common type
# It finds a common type for all the elements to be converted to

# Because all elements of an array have the same type,
# arrays itself have what is called a dtype, short for data type
print(my_array.dtype) # int
print(my_array2.dtype) # U21

# Other examples: 
float_array = np.array([3.14,2.16,1.5])
print(float_array.dtype) # float64
int_array = np.array([1,2,3])
print(int_array.dtype) # int64

# Second distinction between lists:
# Arrays have a fixed size
# You cannot add or remove elements from an array after it was created
my_list2 = [1,2,3,4,5]
my_list2.pop()
print(my_list2) # The pop() has removed the last element of the list
my_list2.append(6)
print(my_list2) # The append has added an element to the list

# What about arrays now
my_array = np.array([1,2,3,4,5])
my_array.pop() # Attribute Error, no pop for arrays
my_array.append() # Same for append
my_array.insert()
# All of the methods that allow you to insert, remove, or append elements to lists
# do not exist on arrays

# Instead, you need to use funcitons to create new arrays:
my_bigger_array = np.append(my_array, 6)
# This will create a new array that has the same content
# as my_array, plus the element 6 appended to the end
print(my_array) # Unchanged: Sill 1,2,3,4,5
print(my_bigger_array) # A new array was created

# Summary: Arrays are more constrained. They have to have the same data type
# They have a fixed length

# These restrictions enable very powerful things

# Let me show you:
# First, let's not use arrays
prices = [9.99,19.99,4.99,14.99,24.99]
quantities = [120,75,300,50,40]
# Say I want to calculate, for each product, the total revenue: price * quantity
# for each of these five products
# How would I do that

revenue = []
for (p,q) in zip(prices, quantities):
    revenue.append(p*q)
revenue # Can't really see it, but this operation is sloooooow

# What arrays allow you is to do vectorized operations. Rather than taking the elements
# one by one and checking, one by one, if the operation is allowed and how it works,
# arrays are going to perform all the alculations at onece on all the elements

arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
arr_totals = arr_prices * arr_quantities
print(arr_totals) # I can just multiply the arrays directly

# Other examples:
units_jan = np.array([120,75,300,50,40])
units_feb = np.array([150,60,330,80,25]) # Units sold for 5 different products, in Jan and Feb
totals = units_jan + units_feb
print(totals)
# How much more or less we sold in Feb compared to Jan
print(units_feb-units_jan)
# Growth rate over the two months?
print(units_feb/units_jan)

# A restriction though!
units_jan = np.array([120,75,300,50,40])
units_feb = np.array([150,60,330,80]) # Only four products this time!
print(units_feb-units_jan) # Value error, two arrays are of inequal length
# The number of elements in an array is called the SHAPE:
units_jan.shape # 5
units_feb.shape # 4. To sum, divide, or multiply two arrays, they need to have
# compatible shapes. This is why we cannot add or removed elements from arrays
# We need to know their shape at all times

# What else can we do with arrays?
# We can compare them
units_jan = np.array([120,75,300,50,40])
units_feb = np.array([150,60,330,80,25]) 

feb_sold_more = units_feb > units_jan
print(feb_sold_more)

# You can square an array
print(units_jan **2) # Again applies the operation in a vectorized way to each element

# You can also use the square root (if we are careful to use the numpy version)
print(np.sqrt(units_jan)) # the numpy library contains special versions of common math
# operations that are specifically designed to work with arrays

# Error: We recorded 10 fake transactions for each of the products in Jan:
print(units_jan - 10)

# There are many operations you can apply to arrays... and arrays also have methods
# that you can inspect!
units_jan.mean() # Returns the mean... if the array has a numeric datatype
units_jan.max() # Returns max value
units_jan.std() # Returns stdev

# We've already seen that you can index and slice arrays like lists:
prices = np.array([10,5,20,30,8])
print(prices[0]) # First price
print(prices[0:3]) # First three prices
# When you index with a single value, you get a value of the dtype of the array
# When you slice an array, you get a new array

# When working with arrays, like with lists, you can edit the elements of the array
# Let's replace the first price by 15:
prices[0] = 15
prices
# What if we want to now make the first two prices equal to 15 and 7
prices[0:2] = [15,7]
prices
# Arrays are still mutable! We just cannot change their shape.

# Everything that we've seen so far with indexing and slicing
# is identical to what we could with lists

# We can do more powerful stuff with arrays!
# 1. 'MASKING' or 'BOOLEAN INDEXING'
# We can index an array with a Boolean array of the same shape
my_mask = np.array([True,False,True,False,True])
prices = np.array([15,7,20,30,8])
# I have my array, and my mask array
print(prices[my_mask]) # I can index the prices using the mask: put the mask
# between square brackets after the array
# When you index with a mask, you are going to get in return only the avlues of the array
# where the corresponding position in the mask is True
# Think of overlapping the mask on top of the array: The True are the cutouts
# Any value that is in the cutout is going to be returned

# When are masks useful
quantities = np.array([5,10,15,-5,-7,10]) # Quantities cannot be negative, so this
# array contains some coding errors
# Could we create a mask that would reveal these errors?
my_mask = quantities >= 0
print(quantities[my_mask])
# How can we use it to spot all the erroneous values in quantities
bad_mask = quantities < 0
print(quantities[bad_mask]) # We used the mask to see all the negative values
# in quantities, and get them in an array
# Now, can we use the mask to replace all these negative values by 0
quantities[bad_mask] = 0 # You use the mask to highlight all the negative values
# and you assign the value 0 to them
quantities

quantities = np.array([5,10,15,0,0,10]) # This is the number of customers a coffee shop
# had Monday through Saturday?
# 1. On average, how many customers did they see on these six days? Reminder: .mean()
# is a method that gives you the mean of an array
quantities.mean() # 6.667
# 2. On all the days they say at least one customer, how many customers did they see
# on average?
new_mask = quantities > 0 
print(quantities[new_mask].mean()) # 10

# You can also do this in a one-liner
quantities[quantities > 0].mean() # Whatever object is between [] is the mask:
# We don't need to store it in a variable first

# Final thing with arrays: Fancy Indexing... and that's pretty fancy
# Let's say you have emails from four customers:
emails = np.array(["quentin.andre@colorado.edu",
          "gal@yale.edu",
          "puntoni@wharton.edu",
          "gino@hbs.edu"])
emails[0] # first email
emails[0:2] # first two
# With lists, you can only index with a single value or use a slice
# With arrays, you can index with multiple values
# That's what fancy indexing is:
print(emails[[0,0,1,2,0]]) # You give a list of values as an index
# Note the double bracket: first set to index, second to define the list
# If it makes it easier, you can break it down to two lines
my_indices = [0,0,1,2,0]
print(emails[my_indices])

# Why fancy indices? Very common: select a random example of rows in a dataset

# Let's wrap upp on arrays:

# 1. An array is a new type of iterable, it works a lot like a list
# 2. Exception 1: Arrays only contain values of the same type. The data type of an array
# is called its dtype
# 3. Exception 2: Arrays have a fixed shape. They can't be pop(), append(), or insert()
# 4. Thanks to these restrictions, arrays can be added or subtracted from each other,
# its elements can be multiplied, squared, divided, exponentiated, whatever you want
# These operations are performed on all elements of the array are much faster
# 5. Arrays can be compared, element-wise, to create Boolean arrays, also called masks
# 6. You can use the masks to filter arrays and re-assign values at specific positions
# 7. Arrays, like lists, can be index and sliced, both to select and replace values
# 8. Compared to lists, arrays accept two new forms of indexing: Boolean indexing
# (only the values facing the True values in the masks are returned), and Fancy Indexing
# (all the indices specificed in the list are returned)