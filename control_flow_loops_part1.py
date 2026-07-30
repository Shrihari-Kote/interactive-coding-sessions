# Loops are code blocks that are going to run multiple times.
# We are going to learn/relearn about two different kinds of loops
# While loops, and for loops

# Let's start with the while loop:
count = 0
while count < 5: # While keyword, followed by a conditional statement
    print(count)
    count = count + 1

# A while loop is going to execute as long as the condition is True
# As soon as the condition becomes False, it will no longer run
# That means a while loop run zero, one two, .... infinitely many times

# The typical structure of a while loop:
# Step 0, Initialization: The condition must be equal to something.
# Step 1, Condition Change: Inside the loop, something will happen to the condition
# If this step is ignored and the condition is never changed, the loop runs forever

# A very common use case for the while loop is to WAIT until some condition becomes TRUE:

user_input = "" # Initialization

while user_input == "":
    user_input = input("Please enter something: ")
    print("You entered " + user_input)

# Let's use a while loop to process a to-do list:
to_do = ["laundry",'dishes','yard cleaning','dog walking'] # Initialization:
while len(to_do) != 0:
    item = to_do.pop() # Removing the last item of a list, and returns it:
    print("Now I'm doing this: " + item)

# The skill that we are going to practice, and that is important for reading code
# is called TRACING a loop:
# Understanding at each iteration, what happens
# Iteration 0: After iteration 0, what is 'item' equal to? 'dog walking'
# To_do is equal to ["laundry",'dishes','yard cleaning']
# What is len(to_do) equal to? 3
# Thus, the while loop is going to run again. It does this until each item in the
# list has been popped

# One small detour
# f-string time (PAIN)
my_age = 28
my_name = "Shrihari"
my_school = "CU Boulder"
greeting = "Hello, I'm " + my_name + ", I'm " + str(my_age) + " and I'm a student at " + my_school
print(greeting)
# This works, but it is ugly and long to write
# and I need to convert ints and floats to strings
better_greeting = f"Hello, I'm {my_name}, I'm {my_age}, and I attend {my_school}"
better_greeting
# f-strings are based actually, concatenation is cringe

# Now it's time for for loops
# Remember a while loop is something that checks if a condition is True
# and runs so long as that condition is true

# What is a for loop?
# It is something that ITERATES on an object, and runs as many times as the number of elements
# in that object

for number in [1,2,3,4,5]: # It starts with the keyword for
    # then it names a variable (we called it number), called the 'STEP' variable
    # then the in keyword
    # then an ITERABLE: something that contains a number of elements (here the list 1-5)
    # the STEP variable is going to take the value of all the lements
    # in the ITERABLE, one by one
    print(f"The number is {number}")

# A for loop is meant to run a KNOWN number of items: the length of the iterable

for letter in "Shrihari":
    print(letter)

list_of_numbers = [1,2,3,4,5,6]

for i in list_of_numbers:
    square = i**2
    print(f"The square of {i} is {square}")

# Tracing practice
# Iteration 0: i is 1, square is 1, print "The square of 1 is 1"
# Iteration 1: i is 2, square is 4, print "The square of 2 is 4"

# Let's get dangerous
# Here, we were printing the squares
# We didn't save them anywhere
# Let's build another for loop that stores the square in a new list
list_of_squares = [] # This empty list will contain the squares
for i in list_of_numbers:
    square = i**2
    list_of_squares.append(square) # Reminder: .append() adds to the existing list,
    # modifying it in place

# Iteration #, number, square, list_of_squares
# First, 1, 1, [1]
# Second, 2, 4, [1,4]
# Third, 3, 9, [1,4,9]
# ...
# Final, 6, 36, [1,4,9,16,25,36]
list_of_squares

# Let's say we're confused (we're not), we really do not understand how the loop is working
# Q's recommendation: Add a print statement explaining what's going on

for i in list_of_numbers:
    square = i**2
    list_of_squares.append(square)
    print(f"Current iteration: number is {i}, square is {square}, list_of_squares is {list_of_squares}")

# Very common use case for a for loop: Accumulate something.
new_list_of_numbers = [4,8,15,23,42,9]
# I want to now what all these numbers sum to:
total = 0
for i in new_list_of_numbers:
    total = total + i
    print(f"The sum of {new_list_of_numbers} is {total}")

# Let's trace this:
# Iteration #, number, total
# First, 4, 4
# Second, 8, 12
# Third, 15, 27
# Final, 9, 101
print(total == sum(new_list_of_numbers))
# Sum is essentially a for loop that iterates through whatever's listed

# Now let's do a for loop that get us the maximum value in a list of numbers
list_of_nums = [4,-3,9,-7,14,52]
max_value = -1000
for x in list_of_nums:
    if x > max_value:
        max_value = x
        print(max_value)
    # If else is smaller than the current max, we don't care, so we don't need an else

# Iteration, x, max value
# First, 4, 4
# Second, -3, 4
# Third, 9, 9
# Fourth, -7, 9
# Fifth, 14, 14
# Final, 52, 52