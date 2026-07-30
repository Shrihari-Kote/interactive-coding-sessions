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