# Today we talk about collections
# Collections are objects made to hold other objects inside them
# They are bags of different kinds

# First, lists

# A list is an ordered collection of items
# It is created using square brackets

my_empty_list = [] # This is a list that contains nothing
type(my_empty_list) # A list! A new kind of object!
# What do lists do? They contain other objects

my_favorite_numbers = [1,2,3,4,5]
print(my_favorite_numbers)

# Lists can contain other elements!
my_favorite_colors = ["red","blue","green"] # A list of strings
my_favorite_decimals = [3,14,2.718,1.618] # A list of floats
my_favorite_booleans = [True,False,True] # Lists can contain repeated elements

# Lists can contain elements of different kinds
my_favorite_things = ["red", 3.14, 2, False]

# You can put anything you want in a list, including other lists!
my_mixed_list = [False, ["blue, 19"], ["red", False], 3.14]
# Don't be surprised, lists are very flexible.  You can put a lot of things in them.

# Lists are objects meaning - they contain properties and methods!
 #L Let's some methods of lists

my_favorite_colors.append('yellow')
# This does not print anything, just adds a value to the list
print(my_favorite_colors)
# It contains yellow! A new item was added to it

# This method 'append' is extremely different from all the other methods that 
# we saw before, on strings for instance. Why?

# Because it CHANGED the object directly. It 'mutated' the original object.
# Memory refresh time (gem alert)
my_string = "shrihari"
# What happens if I do:
my_string.upper() # Running this prints a string in upper case
print(my_string) # The original string is still in lower case
# In technical terms, the method COPIES the original object, changes it, and returns
# the copy. The original NEVER changed.

# This is because strings are 'immutable.' Once created, their content won't change.
# The only way to change a string is to create a new one with different content.

# Back to lists: Let's see how methods affect them
my_favorite_colors # Now contains red, blue, green, and yellow
print(my_favorite_colors)
# I am going to run the append method again to add another color: pink.
a = my_favorite_colors.append('pink')
my_favorite_colors
print(a)
# The method MUTATED the original list, even despite the 'a = '
# WHat is inside a? NOTHING!
# When you are working with a method that mutates the original, it will not
# typically return the original. It will do something on the original,
# and return 'none'.

# VERY CONFUSING WONT BE ON EXAM BUT WORTH KNOWING

# Let's say we don't like that. We don't like the fact that every time we add things
# to my favorite colors, it changes the original.
my_original_colors = ['pink, purple']
# I want to add a color to this list, but not modify the original
my_updated_colors = my_original_colors # I want my original colors to be my backup
# Cool, now I can add something to my updated colors and my original colors will 
# still exist somewhere
my_updated_colors.append('orange')
my_updated_colors
# Now what of my original colors?
my_original_colors
# IT DOESN"T WOOOOOOOOOOORK
# It prints the list with orange anyway, because lists are mutable, so when you do a
# list1 = list2 it still points to the same list, rather than creating a copy
# If you don't want that, you have to use the copy() to create a copy of the list
my_original_colors.copy()

# Back to less confusing things
# Other methods with lists:
my_favorite_colors
# What if you want to remove an element of the list?
# You can use a method called 'pop()'. Pop is going to remove the last element of the list
# AND RETURNS IT to you
removed_color = my_favorite_colors.pop()
# Before running - what will be the content of my favorite colors?
# I say red blue green yellow
my_favorite_colors # I am right
removed_color
# removed_color is pink, because pop actually returns a value

# What if I rerun the line?
removed_color = my_favorite_colors.pop()
my_favorite_colors
removed_color # It removes yellw from the list and returns it to us
# This means that my favorite colors is now red blue and green, and removed color
# is just yellow

# Something new with lists: If you run the same command multiple times, the behavior
# will change. The list is being mutated, so you are not going to get the same results.

# What happens if you don't assign the popped color to a variable?
my_favorite_colors.pop() # It removes green and prints it
# This is a behavior that we've seen before. If a function or method returns something
# and we don't 'catch' it in a variable, it 'falls' into the terminal
my_favorite_colors # The list now only contains red and blue

# Lists are ordered, meaning you can reach into them at a specific position
# and grab specific content
my_favorite_names = ["Shrihari", "Nick", "Ali"]
# Let's say that I want to read what is at the beginning of that list?
# If you want to get an element, you can use an operation called INDEXING
# Indexing is: you put square brackets after the list, and use the index of the element
# that you want to grab - and this is just bracket notation
print(my_favorite_names[1]) # R starts counting from one, Python from 0
# 0 returns the first element, 1 the 2nd, etc., so it returns Nick
print(my_favorite_names[0])

# What happens if you index [3] which does not exist?
print(my_favorite_names[3]) # IndexError

# Let's continue our discussion of INDEXING
# We can also use NEGATIVE indices:
print(my_favorite_names[-1]) # -1 reads the last value (time is a flat circle)
# -2 reads the second to last value, etc.

# We can also do something called SLICING to grab multiple values
# from a list:
my_favorite_numbers = [1,2,3,4,5,6,7,8,9,10]
# Indexing again first:
my_favorite_numbers[2] # Gets the third value of the list (3)
# Slicing:
# The syntax for slicing is [start:stop:step]. Let's see what that means:
my_favorite_numbers[0:3:1] # I assume this means every object between the first and fourth
# objects in the list, not including the fourth (1 = 1 step)
# More examples
my_favorite_numbers[1:6:1] # Every object between the second and seventh:
# not including the seventh
my_favorite_numbers[3:8:1] # Every object between the fourth and eighth (exlcude ninth)
my_favorite_numbers[0:6:2] # Every second object between the first and sixth, starting
# with the first, so 1,3,5

# When you are slicing, you can omit some arguments
my_favorite_numbers[0:3] # The default step count is '1' if omitted 
# This is equivalent to [0:3:1]
# What about this, if you omit the first or second bound:
my_favorite_numbers[1:] # All of them starting from index point 1 (the second number)
# Thus we get 2-10
my_favorite_numbers[:4] # All numbers between index point 0 and 4, so 1-4
my_favorite_numbers[::2] # Both start and stop are omitted, so it starts with 0 and
# includes every other value (this should give all odds)
my_favorite_numbers[::-1] # This actually counts backwards, and it does the whole list

# Want to see something cool?
my_name = "Shrihari Kote"
my_name_but_mirrored = my_name[::-1]
my_name_but_mirrored # Holy Zatanna Batman, you can slice strings too!
my_name[0:4] # This lists the first 4 letters in the string "Shri"

# So far, we learned that
# 1) lists are mutable, meaning we can modify their content using methods
# 2) lists are iterable, meaning we can select a subset of their content using slices

# Let's mash these two things together!
my_favorite_names
# It's weird to have my own name in my favorite, let's replace it  with something else.
# How could I repalce "Shrihari" with 'Adam' in this list
my_favorite_names[0] = 'Adam' # Indexing the first element of the list allows us
# to assign the value 'Adam' at that position
my_favorite_names # The list is mutated!

# We can do the same thing with slices!
my_favorite_names[1:] # This is slicing ['Nick', 'Ali']
my_favorite_names[1:] = ['Eve', 'Joshua'] # Two objects must be given
my_favorite_names # We can use slicing and indexing to read or update the content
# of a list

# Bonus question: Can we use indexing or slicing to update the content of a string?
my_name[0] = "Z" # NOPE, because strings are immutable!
# To make a modified string, you have to create a new string

# Back to a few list methods:
my_favorite_names.pop() # Removes the last element of a list
my_favorite_names.append('Joshua') # Add this element at the end of a list
# Pop can take an additionl argument: position!
my_favorite_names.pop(0) # This returns Adam because that is the first object in the list
my_favorite_names.insert(0, 'Adam')
my_favorite_names # Must use insert for positions outside the last, append only does last
# All these methods modify the original list, not returning a copy of the original
# Let's try one more:
my_favorite_names.reverse() # This does not return anything, it changes the order of
# the original list

# Lists are collections of ordered items
# Dictionaries are collections of key:value pairs

# Example to start with:
my_friends_age = {'Nick': 40, "Sam": 35, "Juan": 37}
# Note syntax: CURLY brackets, containing key:value pairs, separated by commas

#Dictionaries can have different kinds of values:
my_information = {'name': "Shrihari", "age": 28, "hobbies": ["reading","gaming"]}
# Here you have a the key 'name' which has a string value
# The key 'age' which has a number
# And the key 'hobbies' which has a list value

# What about the keys in a dictionary? What can they be?
# They are typically int or str. The most important rules:
# They have to be UNIQUE (only one key must have a given name)
# and they have to IMMUTABLE (lists can't be keys)

# How do you use dictionaries?
# We can reach inside them to see the values using INDEXING!
# For a list it is ordered, so we index with numbers
# Dictionaries are not ordered, so we index using the keys

my_friends_age["Nick"] # Nick's age outputs the value 40
# Using square brackets to index, and using the key gets the value

# What will I get if I type this?
my_information['hobbies'] # My guess is a list. I was right.

# Dictionaries like lists, are mutable. We can update them.
# Let's say Nick just celebrated his birthday
# How do I update his age?
my_friends_age["Nick"] = 41
my_friends_age # It has been updated to show that 'Nick' = 41

# Let's try another example; can I change my name to "Shrihari Kote"
my_information["name"] = "Shrihari Kote" 
my_information # Basically the same as changing Nick's age to 41, but with a string
# instead of an integer

# We can add new keys to a dictionary using the same syntax
my_information['job title'] = 'MSBA student'
my_information

# We can use indexing to
# 1. Read the value of an existing key
# 2. Update the value of an exisitng key
# 3. Create a key with a given value

# To remove a key:value pair:

del my_information['job title']
# OR, because dictionaries are OBJECTS, they have METHODS!!!!1
my_information.pop('job title')
my_information

# First useful method: get()
# If you index a dictionary with a value that does not exist, what happens?
my_information['address'] # If you check for a value that does not exist, you will 
# get a KeyError
# Errors are bad because they will stop your code's execution
# A better way to check if a key exists is to use .get()
shrihari_address = my_information.get('address')
print(shrihari_address) # This will print none, because get() returns a None value
# when they key is not found. None is a valid value, which is better than getting an error

# Three other useful methods: rather than blindly checking if a key exists, sometimes
# you want to see all they keys in a dictionary
my_information.keys()
# You can do the same thing with values with... well, values()
my_information.values()
# You can know all the keys, all the values, but not to which each correspond
# Solution? Trivago.
my_information.items() # Gives all key-value pairs in the dictionary

# Reminder: The keys of dictionaries must be int or str
# The values can be anything. So far we've seen:
# str values
# int values
# list values

# What is very common is to have dictionaries as values, to sto more complex inforomation
# Example
my_friends_info = {
    "Nick": {
        "age": 41,
        'city':  'Boulder',
        'hobbies': ['skiing', 'cooking'] 
    },
    "Sam": {
        "age": 35,
        'city':  'Chicago',
        'hobbies': ['hiking', 'coffee'],
        'job': "professor" 
    }
}

# How would we use a dictionary like this, with nested dictionaries inside?
# How would you get your friend Nick's information?

my_friends_info["Nick"]
# We just got Nick's dictionary!
# How do we extract his age from it? More brackets babyyyyy 
# Nesting the brackets DOES NOT WORK
my_friends_info["Nick"]['age'] # We index Nick's dictionary to get his age
# How do we get Sam's hobbies?
my_friends_info['Sam']['hobbies']
# What if you're not sure if you have information about a friend's job? Use .get()
my_friends_info['Nick'].get('job') # Nothing because he has no job (sadge)
my_friends_info['Sam'].get('job') # We get professor!

# Mini assignment. Sam recently picked up birdwatching. How to add this hobby to the list?
# Hint: use append()

my_friends_info['Sam']['hobbies'].append('birdwatching')
my_friends_info['Sam']['hobbies'] # Yep it worked

# Lists are ordererd collections of elements of any kind
# We manipulate lists using INDEXING AND SLICING to access and modify the elements they contain
# We can also use methods like .pop(), .append(), or .insert() to do that

# Dictionaries are UNORDERED collections of key:value pairs
# We access the values by their key
# We manipulate dictionaries using INDEXING to access and modify the values
# associated with given keys

my_friends_info[0] # There is no key called 0, so indexing returns a KeyError