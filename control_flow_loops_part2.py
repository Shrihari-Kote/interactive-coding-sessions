# You can consider these advanced topcis in loops

# One thing i said is that, in a for loop, the thing that we are looping over:
#for x in the_thing_that_we_are_looping_over: is called in ITERABLE
# An iterable means: something that we can unpack into distinctive elements

# We've seen some: lists are iterable:
fruits = ['banana','apple','mango']
for f in fruits:
    print(f)

# We've also ween that strings are iterable:
my_word = "Supercalifragilisticexpialidocious"
for letter in my_word:
    print(letter)
# When you loop over a string, you are getting the letters one by one

# Dictionaries are also iterable
my_info = {"name":"Shrihari", "age":28, "city":"Boulder"}
for info in my_info:
    print(info)
# This prints the dictionary's keys

# How to print both keys and values?
for key in my_info:
    value = my_info[key]
    print(f"The key is {key} and the value is {value}")

# Easier way:
my_info.items() # This gives you each key:value pair in succession

# We can actually iterate using this method!
for (key, value) in my_info.items():
    print(f"The key is {key} and the value is {value}")

# Simpler examples of unpacking:
fruits = ['banana','appple','mango'] # List has three items
fruit1, fruit2, fruit3 = fruits # Three variables for three items
fruit1

# Let's say I want a loop that prints me:
# Fruit 1: banana
# Fruit 2: mango
# Fruit 3: apple

for (index, item) in enumerate(fruits):
    # When, instead of iterating on the ITERABLE directly
    # we used enumerate(ITERABLE), we are getting both the index and the element
    # at each loop
    print(f"The element at position {index + 1} is {item}")

# FINAL
# Let's say we have multiple lists thare somehow connected to each other
list_of_foods = ['pickle','pepper','cherry']
list_of_tastes = ['sour','spicy','sweet']

# Here we might want to print: "a pickle is sour", "a pepper is spicy"
# THere is a command for connecting, "zipping", multiple variables together:

for (food,taste) in zip(list_of_foods,list_of_tastes):
    # At each iteration, we are getting one element of each list,
    # unpacked into their respective step variable.
    print(f"A {food} is {taste}")

# What if we have THREE lists?!
list_of_colors = ['green','red','red']
for (food,taste,color) in zip(list_of_foods,list_of_tastes,list_of_colors):
    print(f"A {food} is {color} and tastes {taste}")

# Let's talk about range()

for i in [1,2,3,4,5]: # i is the STEP VARIABLE, [1,2,3,4,5] is the iterable
    print(i) # i is going to take, in turn, the value of each of
    #the elements in the iterable

# Now imagine we want to get all the numbers from 0 to 1000:
# Writing the loop the old way sucks, because you'd have to write out each number
# manually, which defeats the whole point

# Enter range()
# Range is a funciton that creates an iterable for you that you can loop on
# Range takes three arguments (start, stop, step)
# Start is optional, defaults to 0
# Step is optional, and defaults to 1
for i in range(1001): # This prints every number between 0 and 1000 (1001 not included)
    print(i)

# The start, stop, step system is just like slicing from lists
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list[0:4]
my_list[::2]
for i in range(0,1000,2):
    print(i)

# All there is to know about range: a convenient way
# of getting an iterable of numbers to loop on

# The final thing he wants to show us is something called list comprehensions

# Let's say we want the square of every number between 0 and 9

my_squares = []
for i in range(0,10,1): # Could've done range(10) that's more compact
    my_squares.append(i**2)

my_squares

# This task, creating a new list from an existing iterable, is EXTREMELY COMMON
# in Python
# That's what a shortcut called LIST COMPREHENSION is doing
# I could have achieved the same thing by typing:
my_squares = [i**2 for i in range(10)]

# Back in my day we'd have solved this with a one-liner in PERL! WITH A BOX OF SCRAPS

# A list comprehension is surrounded by square brackets
# This is because we are creating a list
# Then you see AN EXPRESSION: i**2. This defines how the step variable is going
# to be modified to create the elements of the list
# Finally, you see the loop itself: for STEP_VARIABLE in ITERABLE
# Note, there is no colon here
my_squares

my_list = [i.upper() for i in "Shrihari"]
my_list

# One final thing on list comprehension:
# We can add, after the (for STEP_VARIABLE in ITERABLE) an optional IF statement
# that filters the leemnts of the list

my_filtered_squares = [i**2 for i in range(10) if i**2 < 30]
my_filtered_squares

# Very common use case for this filter:
paths = ["data.csv","report.pdf","summary.csv","image.png","notes.txt","data2.csv"]
# Lots of file names with different extensions

# Let's say I just want to keep the .csv files

my_csvs = [i for i in paths if i.endswith("csv")]
my_csvs

# How could I write a for loop that would do the same job:
my_csvs2 = []

for i in paths:
    if i.endswith("csv"):
        my_csvs2.append(i)

print(my_csvs2)
