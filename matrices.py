import numpy as np
# This is a one-dimensional array:
one_d = np.array([1,2,3,4,5])
# Remember: we can use the property shape to see the shape of an array:
print(one_d.shape)

# The innovation for this morning: We are going to introduce 2-d
# arrays. A 2-d array is like a matrix with rows and columns

# How do we create a 2-d array?
# like this:

two_d = np.array( # Here I also have a single argumen.
    [[1,2,3],
    [4,5,6]]
) # Basically, two layers of brackets. I have a list that contains three lists
# Each of these inside lists correspond to a row of values in the matrix

print(two_d) # It shows a matrix with rows and columns
# How many rows: The number of lists inside
# How many columns: The number of elements in inside these lists

print(two_d.shape)
# The first number of .shape is always the number of rows
# The second nmber is always the number of columns
# Order: ROWS, COLUMNS

# Try to predict what happens if you index a 2-D array?
print(two_d[0]) # I predicted that you'd get the first element of the first list
# The actual answer is that you get the whole first list/row. This is a one-dimensional
# array
print(two_d[1]) # This nets you the second list/row

# So far, it's exactly like what we saw with lists and one-d array:
# When you index with a number you get the corresponding element
print(two_d[0:2]) # I predict the first two rows, and I was right!
# You can also slice a 2-d array, and it works in the same way

# So what's new then?
# Since 2-D arrays have two dimensions, we can use two sets of indices separated
# by a comma; the first for the rows, the second one for the columns
print(two_d[0,0]) # I imagine this gives me row 1 column 1
print(two_d[1,1]) # Row 2 column 2 (5)

# Let's practice a few more:
print(two_d[0,0:2]) # First row, first two columns
print(two_d[1,1:2]) # Second row, second column
print(two_d[1:2,1:3]) # Second row, second and third columns
print(two_d[-1,-1]) # Last (third) row, last (third) column
# If you use a slice, you keep that dimension
# If you use a index, you just get a single element

# I'm going to introduce a new notation:
print(two_d[:,0]) # Just an empy colon, called an empty slice,
# You get all the elements, here meaning all rows, and only the first column
# This is a one-d array

two_d = np.array(
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
)

# Like on 1-D array, we can use slices and indexing to replace values
# Exercise: Replace 5 with 999 via indexing

two_d[1,1] = 999
print(two_d)
# Now make the final column 7,14,21

two_d[:,2] = [7,14,21] # Can also use two_d[:,-1] = [7,14,21]
print(two_d)

# Let's restore the original array
two_d = np.array(
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
)

# 2D arrays are arrays, meaning we can do the same thing we saw
# Tuesday on 1D arrays

# Can you create an array that flags all the value in two_d
# that are greater than 5 (strictly greater)

mask = two_d > 5
mask
print(two_d[mask])

# Can we use this mask to replace all values greater than 5 with 999?
two_d[mask] = 999
print(two_d)

# let's recreate the matrix again
two_d = np.array(
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
)

mask = two_d > 5
print(mask)

# More examples

a = np.array([[1,2],
              [3,4]])
b = np.array(
    [
        [1,1],
        [2,4]
    ]
)

# We already saw that we can add arrays when they have compatible shapes
print(a+b)
# Subtract them
print(a-b)
# Multiply them:
print(a*b)
# Divide them:
print(a/b)
# You can add a single number to them
print(a+10)

# Final thing I want to teach you:
# On tuesday, we saw that arrays have methods:
one_d = np.array([1,2,3,4,5])
print(one_d.sum())
print(one_d.max())

# Two-D arrays also have methods... with a very small twist
units_sold = np.array([
    [120,150,130,170],
    [75,60,90,80],
    [300,330,310,350]
]) # One thing not mentioned: when creating an array, all the rows
# need to have the same number of elements
print(units_sold)
print(units_sold.sum()) # This is the grand sum, of all products sold in all months

# What if instead we wanted to have the total per product
# Or the total per month
# This is where a nifty keyword comes in: axis = 
# This is an argument on most array methods

print(units_sold.sum(axis=0))
# The axis tells us the dimension that we are collapsing
# That we are taking the method over
# Here, we sum the dimension 0 (the rows) and are thus left with the columns
print(units_sold.sum(axis=1))
# Here we do the opposite: we take the sum across the columns, and are left with the rows

# Exercise: The method mean() gives you the mean of an array
# It also takes an optional axis argument
# Use this method to give me the mean units sold in each of the four months
print(units_sold.mean(axis=0))

# Using the method max, find the best performing product and month combo
print(units_sold.max())

# Final exercise: Find the minimum number of sales for product A across all four months
print(units_sold[0,:].min())