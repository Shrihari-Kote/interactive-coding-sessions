import pandas as pd

# So what is a dataframe? We are going to star from a familiar object
# to understand what it is and what it does

data = {
    "Month": ["January","February","March","April"],
    "Marketing_Spend": [2000,3000,2500,4000],
    "Sales_Spend": [5000,7000,6000,8000],
    "Leads_Generated": [150,200,180,250]
}
# A dictionary where the keys are column names
# and the values are lists OR arrays, containing the column values
# Most important: All these lists/arrays must have the same size
# They determine how many rows you have in your data

# Now that we have this data, we can create a dataframe as such
df = pd.DataFrame(data)
df

# In practice turning dictionaries into dataframes is bad form
# Read data from csvs like a normal person

sales = pd.read_csv("sales_data.csv") # Use relative path if you can
# Now that we read it, let's see what is in our dataframe
print(sales)
# This dataset is small, 12 rows only
# If you print a df with 100k or more rows the terminal might crash
# Just use head method (it's like head in R, but not a function)
sales.head() # First five rows
# For good measure, you can also check the end of your data
sales.tail() # Last five rows

# If you want a richer summary, you can can use .info()
print(sales.info())

# You can access a bunch of these things individually
print(sales.columns) # Column names
print(sales.shape) # Shape of df
print(sales.dtypes) # Name of columns AND corresponding datatypes

print(sales.index) # THe index in a df is "the names of the rows"
# By default, when a dataset is made or read in, the rows are going to be assinged
# names using a range(): First row will be 0, second will be 1, and so on

# A dataframe is:
# AN index, containing the name of the rows,
# A list of column names, containing the name of the columns
# A collection of arrays, mapped to individual column names
# Like a mix of a dictionary and arrays (key:value, except the values are arrays)

# How do you index a dataframe
# How do you access individual rows and columns of the dataframe
# for reading and writing data

# Let's first start easy: How do you read the content of a column in a dataframe
# Remember that dataframes are a lot like dictionaries:
sales["Month"] # I index by the name of the column, and get the content of the
# colum back. A column in a df is called a series. For all intents and purposes
# it's going to work like an array, with row indices in front of each value

print(sales["Marketing_Spend"])

print(sales[["Month","Marketing_Spend"]]) # Note the double brackets, one to say 
# that we are indexing, one to say: a list with multiple elements
# When you ask for multiple columns, you get a dataframe back

# Much like on arrays, we can then replace the content of a column:

sales["Marketing_Spend"] = sales["Marketing_Spend"] * 1.1 # We get the content of the
# column marketing spend, multiply it by 1.1, and store it back into the df

# We can also create new columns!
# To add a new key to the dictionary, we simply did: my_dict['new_key'] = 'value
# We use the same logic to create new columns in dataframes
sales["Cost_Per_Lead"] = sales["Leads_Generated"]/sales["Marketing_Spend"]
sales.head()

# We saw how to index columns. Useful!
# Next, how do we index rows?

# A typical reason why you would want to index is to identify rows
# that have a specific condition. THat's called filtering data

# Let's say you want to flag the months/rows where the cost_per_lead was cheap
# say < 15

mask = sales["Cost_Per_Lead"]<15
sales[mask]
sales[sales["Cost_Per_Lead"]<15] # Without making the mask

# Apparently this is confusing...
# We can index with column names, and it works...
# and we can also index with a Boolean mask on the rows, and it work as well

# sales["Cost_Per_Lead"] <- Gives me all the rows for this column only
# sales[mask] <- Gives me only the rows where the mask is True, and all the columns

# It is not super clean, and potentially confusing, to use the same way of indxing
# both to get rows and columns

# On matrices, we were doing two_d[row_index,col_index], which was cleaner!

# Let's see how we can have the same syntax on a dataframe

# To do that, you type: sales.loc[row_index,col_index]
# For instance, if I want a particular column all rows, I type:
sales.loc[:,["Month","Marketing_Spend"]]
# If I want just the rows that I masked, all columns, I type:
sales.loc[mask,:]
# And if I want just one column for the rows I masked, I type
sales.loc[mask,"Month"]

# Final topic: Analyzing data

# Both dataframes and series (a series is a single column in a df) contain
# methods for calculating stuff

sales.loc[:,"Cost_Per_Lead"].mean() # This gives the series Cost_Per_Lead with all rows
# .mean() will return mean cost per lead across all rows

sales.loc[:,"Leads_Generated"].max() # 300 is the highest number of Leads Generated

# Methods on series work in exactly the same way as methods on arrays: They return the mean()
# max(), min() value taken across all values

# What if you used these methods on dfs instead, meaning when you have multiple columns
sales.loc[:,["Marketing_Spend","Sales_Spend"]].max() # This gives a dataframe awith all 
# rows and two columns. WHat happens if I call max() on it?
# When you call a method like max or min on a df that has multiple columns
# the default behavior is: calculating across the rows for each of the columns
# Here we are getting the max value for marketing spend and the max value for sales spend

# What if I do this?
sales.loc[:,["Marketing_Spend","Sales_Spend"]].sum() # Same behavior: We are taking the
# sum across all the rows, for each of the two columns. We are getting one sum, across
# the 12 months for marketing spend and another sum across all months for sales spend

# What if, instead, I wanted the total spend for each month?
# Meaning, we sum spend values across columns (along a single row)
sales.loc[:,["Marketing_Spend","Sales_Spend"]].sum(axis=1) # We are collapsing all the
# columns and keeping the rows. We are taking the sum of marketing + sales spend
# for each of the rows

# Now that we have calculated this total, we can save it in our dataframe
sales["Total_Spend"] = sales.loc[:,["Marketing_Spend","Sales_Spend"]].sum(axis=1)
sales.head()

# To summarize again: by default, methods on dfs are applied across rows, for each
# of the columns. If we want to instead apply across columns for each of the rows
# we use axis=1 as argument

# Congrats, we have loaded data, manipulated rows and columns, and created two new
# columns.
# Now let's save our new dataframe into a file
sales.to_csv("clean_sales_data.csv", index=False)