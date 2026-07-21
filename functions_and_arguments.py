# We've been using functions from the start
# print(), type(), round(), str(). etc.
len("Shrihari") # Number of elements in a string or sequence

# What is a function? It is like a machine, it does something
# It usually takes one or more inputs, and usually returns a result

# print() <- what does it take as input?
# Any expression we want to print
# What does it do? It prints stuff to the user.

# str() <- what does it take?
# It takes any expression
# What does it do? It turns the input into a string, and returns it (not prints it)
# to the user

# What does it mean to return something?
# Let's use print as an example
print('1234')
my_content = print('1234')
my_content # This does not work, my_content is empty, print('1234') stored nothing
# Why? 

# Some (most) functions return something. Think of them as a conveyor belt:
# They take an object on side, do something to it, and then RETURN
# the result of what it did on the other side of the machine

# Other functions just do stuff: think of them as an engine
# You put some gas into them, they do something BUT:
# they do not hand you back (RETURN) anything

# Let's write functions together to better understand this distinction
# We are going to write a function that takes a price, a rate, and returns
# the price updated by the rate

def print_total(price, rate): #def followed by function name, parentheses, (arguments)
     # You will see that your cursor moved to the right:
     # this defines the body of the fucntion. Every code inside
     # is going to define what the function will do.
     total = price * (1+rate)
     print(total)

print_total(10,0.1)
# Store a total for later:
my_total = print_total(10,.1)
my_total # Nothing inside my_total. Why? Let's trace the function:
# print_total doesn't return a value, it just prints a value
# Engine, not conveyor belt
# Let's write a better function that solves this issue

def calculate_total(price,rate):
     total = price*(1+rate)
     return total # On the other side of the conveyor belt, spit out the total

my_total = calculate_total(10,.1)
my_total # Success, the function calculated something, returned it, and now I can store it
# If not stored, it just prints it automtically
calculate_total(10,.1)
# Always try to have functions that return things

# More vocab: The inputs of a function are called arguments
# They come in two flavors:
# 1. 'Positional arguments, defined by the order in which you enter them
round (3.14,1)
round (1,3.14) # It breaks because the second argument requires an integer

calculate_total(.1,10) # Position arguments are expected and given in a certain order

# Some functions take a variable number of arguments
round(3.14) # Second argument not compulsory, default is 0
print('ABC')
print('ABC',"DEF","GHI") # Prints with spaces between each string
# Print is an example of a function that can take an infinite number of arugments

# Second flavor of arguments: 'named' or 'keyword' arguments
# These are arguments that are added by specifying their own names
print('A','B','C','D',sep='*')
# Named arguments are not compulsory, and have a default value (for sep it's space)
print('A','B','C','D', sep='-', end="!")

# One final but important thing

def add_excitement(user_string):
     excited_string = user_string + " !!!!!!!!!!!!!!!!!!!!!!!!!!"
     return excited_string

add_excitement("Hello I like trains")

price = 4.50
quantity = 3
total = price * quantity
print(total)

name = "colorado coffee co"
name.title()
brand = name.title()
print(name)
print(brand)

email = " Ada.Lovelace@gmail.com   "
clean = email.strip()
clean = clean.lower()
print(clean)
print(clean.count("a"))

city = "boulder"
print(city.upper())
print(city.upper) # This does nothing
print((19).numerator)

def apply_discount(price,rate):
     discounted = price * (1-rate)
     return round(discounted,2)

print(apply_discount(100,.2))
apply_discount(.2,100)
apply_discount(rate=0.2,price=100)

def show_margin(revenue,cost):
     print(revenue-cost)

def get_margin(revenue,cost):
     return revenue-cost

a = show_margin(500,300)
b = get_margin(500,300)
print(a) # Does nothing because nothing is stored in a, show_margin is a print function
print(b*2)

def unit_price(total,units):
    return total/units
    print("computing unit price...") # print is after return, so it doesn't work

price = unit_price(90,3)
print(price)

# Spot the error

subtotal = 40
print(sub_total * 1.08) # subtotal and sub_total are not the same variable (nameerror)

units = "12"
print(units + 3) # units is a string, can't be added (typeerror)

sku = "ab-1402"
print(sku.uppercase()) # the method is upper() (attributeerror)

price = 10
print(price.numerator()) 
print((price).numerator) # Int error is not callable, need to put it in paranthesis

def label(product,price):
    return product + ": $" + str(price)

print(label(product="latte",price=4.50)) # He was supposed to make this broken but it works
# as written

def line_total(price, quantity):
    return price * quantity

item = "flat white"
price = 4.25
quantity = 2

total = line_total(price, quantity)
label = item.title()
print(label + ": " + "$" + str(total))
tip = round(total *0.2,2)
print(tip)

# All of this is stuff we've gone over before, but it's worth reviewing.