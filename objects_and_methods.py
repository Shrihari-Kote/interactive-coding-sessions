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