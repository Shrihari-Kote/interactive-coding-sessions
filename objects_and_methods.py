this_is_an_integer = 10
this_is_a_string = "Shrihari"
type(this_is_an_integer)
type(this_is_a_string)

# After creating a variable in Python, you can check all the things that are assigned to that
# variable, by typing a dot "." in VSCode
# After you press the dot, it will reveal a list of things
# contained in the object
# These things come in two flavors:
# PROPERTIES: Signaled by the wrench icon, contains information/data
# METHODS: Described by a purple box. Describes all the actions that can be performed
# by the object.
print(this_is_an_integer.numerator) # 10
print(this_is_an_integer.denominator) # 1
# Properties are describing the state of the object that we created
another_integer = 5
print(another_integer.numerator)
# Can we check some properties of the string now
print(this_is_a_string)
# Properties are not very useful for strings

# What is really useful are methods! Which allow us to do stuff with created objects
# They are like functions, in that they do things,
# but are specifically attached ('bound') to the object

# Let's check some out!
this_is_a_string.upper() # methods require parentheses because they are actions
# like a function, so you need to 'call' them
# All strings will have this method. All objects of a given type share the same methods
this_is_a_string.lower()
# We can store the result of that as another variable
my_upper_name = this_is_a_string.upper()
print(my_upper_name)

# Let's see a few more methods for strings
# Strings contain a lot of methods
# Because there are a lot of things that we can do with them
# We've already seen upper(), lower(), title() which capitalizes the first letter
# of each word
my_sentence = 'hello my name is shrihari'
my_sentence.title()
# We've also seen endswith()
my_sentence.endswith('shrihari')
# Let's see some more
lots_of_white_space = "                 Shrihari    "
lots_of_white_space.strip()
# Let's see a practical example of how these methods can be useful
entry = "    shko4431@colorado.edu   "
# This could be something someone entered into a form, badly
# I want to check if this person has a .edu email address
is_it_edu = entry.endswith('edu')
is_it_edu
is_it_edu_for_real = entry.strip().endswith('edu')
is_it_edu_for_real

# You can also write it less neatly by writing entry.stip() to a variable
# and then using endswith on that variable
# WHat I did is called chaining

# Common errors with methods and properties
entry.shout() # AttributeError: no attribute shout()
# You try to call a method that does not exist on the object
price = 12
price.numerator() # TypeError: int object is not callable
type(price.numerator) # Numerator is a property of the integer 12, stored into price
# It contains an integer which is 12
# But an integer does not do anything. It is not a function or a method
# You cannot call it, that's what the 'not callable' is telling you
# The error: Attempting to call a peoprty. You can only call a method inside an object
price.is_integer # This is a method: purple box, and it is an action that we are doing
# What will happen if I run it? Nothing unless the parentheses are there.
price.is_integer()

# We have seen four big types of objects: str, float, int, bool
# In Python you are often going to creat other objects
# Let's see an object solving a problem we had before

from decimal import Decimal # Not seen yet, soon! Don't worry :)
# What is Decimal? It is factory for manufacturing a new kind of objects: Decimals
# To create a str, you put quotes around something
# To create a float or int, you type out a float or int
# To create a boolean, you create a logical comparison or type True or False

#To create a Decimal object, we use the Decimal thingamabob we just imported
a = Decimal(".1")
# We have acreated a new Decimal object, with the value 0.1
type(a)
b = Decimal(".2")
print(.1 + .2) # We get a floating point error
# This is because, by default, Python represents floats with a limited number of zeroes
print(a+b) # The sum of two Decimal objects is an exact representation
# That is the problem Decimal solves
a #If you reach into a Decimal object with the dot, you are going to see
# a lot of new methods and properties