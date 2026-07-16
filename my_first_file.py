print("Hello World")
print(2+2)
# Here nothing gets executed when I press enter
# How can I run this code?
# Two ways:
# 1. Put the caret on a line and press shift + enter
# This sends the line to the REPL in-terminal and runs it
# 2. The second way is to run the file
# Send the entire content of the file to Python, and all of the lines will be executed in sequence
# Press the run button in the top right
# You will want to do this once you've finished writing the script
# Reminder 1: We canmake variables
my_name = "Shrihari Kote"
print(my_name)
# You get a NameError if you don't run both lines of code
# The four big types of data in Python
this_is_an_integer = 3
this_is_a_float = 3.1
this_is_a_string = "Howdy"
this_is_a_boolean = True

# Print values using the print() function
print(this_is_an_integer)
print(this_is_a_float)
print(this_is_a_string, this_is_a_boolean)
# We can print multiple things at once, separated by a comma

# print() is a function. A function is something that takes between 0 and many arguments, and
# has a specific behavior, it is an "action."

# You can print:
# A value:
print(3.14)
print("Hello world")

# A variable:
print(my_name)

# An expression, something that has not been calculated yet:
print(5+6)

# Reminder: Expressions are calculated 'inside out'
# Skill: When reading code, try to always understand what is going to happen
# and in which order. "Tracing the code": Understanding the steps the machine is taking
# to arrive at a result

print(this_is_an_integer)
print(this_is_an_integer + 5)
# 1. The prior line will read the variable 'this_is_an_integer' as equivalent to the integer 3
# 2. It will do the expression 3 + 5, which sums to 8
# 3. It then prints the result

# How do you figure out the type of a variable:
what_is_this = type(this_is_an_integer)
print(what_is_this)
# We can also see that by typing the name of the variable created:
what_is_this
what_is_that = type(3.12)
print(what_is_that)

# Calculations:
print(2+3)
print(2+3*5)
print((2+3)*5)

print(1+2) # This prints 3
print ((1+2) == 3) # This prints the boolean value TRUE

print(0.1 + 0.2)
print((0.1 + 0.2)==0.3)
# Floating point error
# Programming sucks at calculating with decimals
my_rounded_addition = round ((0.1+0.2),1)
# This function takes two arguments: The element to be rounded, and the digits of precision required

print(my_rounded_addition)
round(3.14) #Functions can have non-compulsory inputs

#Logical comparisons
print(3==5) #equals
print(3!=5) #doesn't equal
print(3>5) #greater than
print(3<5) #less than
print (3<=5) #less than or equal to
print(3>=5) #greater than or equal to

# You can combine logical conditions using AND or OR
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) #True
# AND only returns True when all conditions are True
print(condition_1 and condition_3) #False
print(condition_1 and condition_2 and condition_3) #False

# What about OR?
print(condition_1 or condition_2) #True
print(condition_1 or condition_3) #True
print(condition_3 or condition_4) #False
print(True+True) # Trues are 1, Falses are 0, so we get 2
print(True == 1)
print(False == 0)
print(True*5) # 5

# String time

greeting = "Hello" +"world!"
print(greeting)

# This works because with strings, '+' is interpreted as a 'concatenation' operator,'
# a attechnical word for 'putting things next to each other'

laugh = "ha" * 3
print(laugh)

# Multiplication sign is interpreted as a 'repeat' operation

weird_laugh = "ha" + 3.12
# Adding a string to an integer or float does nothing
overly_complicated_laugh = "ha" * ('hello' == 'hello') *3
print(overly_complicated_laugh)
# Do not make things overly complicated
# KISS principle: Keep it simple stupid

# How to keep things simple? We make sure to convert variables before working with them

number = 42
is_this_a_number = "42"
print(number+10)
print(is_this_a_number + 10) # Does not work, cannot add string and number

# Create a new variable:
now_this_is_a_number = int(is_this_a_number)
# int() converts strings into numbers
print(now_this_is_a_number)
print(number + now_this_is_a_number)
int("15") == 15 # True!
int("fifteen") # Error message, cannot interpret letters as a number
int(False) # Counts as 0

# One more example
my_age = 28
my_intro = "Hello, my name is Shrihari, and I am" + my_age # Doesn't work because my_age is an int
my_intro_corrected = "Hello, my name is Shrihari, and I am " + str(my_age)
print(my_intro_corrected)
# str(), float(), int(), and bool() are functions
# which will turn an input into the desired type IF it is possible