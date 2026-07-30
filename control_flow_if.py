# Control flow is a term describing all the tools in Python that voern
# whether, when, and how much/often a block of code is going to run
# Up until now, every line that were writing was running

# First up: Conditional logic
# This is what governs whether a block of code is going to be executed

my_name = "Shrihari"
my_gender = "Male"

if my_gender == "Male": # Conditional logic block always starts with if
    # followed by a condition: It is a statement that will evaluate to true or false
    # The line ends with a colon ":"
    # Then, the line below, you start an indented block:
    # This indented block describes the line(s) of code that will run
    # ONLY if the condition evaluates to true
    # For the most simple conditional logic block, that's all you need.
    # Basically it works the same as R Studio
    # A block with just one IF is binary: Either the block gets executed (if CONDITION is True)
    # or it isn't (if CONDITION is False)
    print("Hello Mr. " + my_name)
    #Sometimes the world is more complicated. There's more than one possibility
    # That's where you can add some bells and whistles to your conditional block
    # using the keywords elif and else
elif my_gender == "Female":
    # It describes a second possible condition
    # That is only going to be checked if the previous conditions evaluated to False
    # It's sequential: We start at the top
    # check if the first condition is True,
    # if it is True, we end here,
    # if it is False, we check the second condition,
    # if it is False, we check the third condition
    # We can have zero, one, or many elif statements
    print("Hello Ms. " + my_name)
elif my_gender == "NB":
    print("Hello " + my_name)
    # Then , at the bottom, after all the elif statements (if any)
    # we can have the else block. The else block means:
    # if all the conditions turned out to be False,
    # here's what you should do
else:
    print("Hello " + my_name + ", how should we address you?")
    # If there is no else statement, nothing happens when all other conditions
    # evaluate to false

# A very common GOTCHA with conditional logic blocks:
# Conditional logic blocks are very common inside functions:
# They allow you to have functions that have a different behavior as a function of their
# inputs:

def status_checker(age):
    # We want this function to return the status of the user
    # As a function of the age that they specify!
    if age >= 13:
        return "You are a teenager"
    elif age >= 18: 
        return "You are an adult"
    elif age >= 4:
        return "You are a child"
    elif age >=2:
        return "You are a toddler"
    else:
        return "You are a baby"

# Let's see how it works
status_checker(1) # You are a baby!
status_checker(3) # You're a toddler!
status_checker(9) # You're a child!
status_checker(14) # You're a teenager!
status_checker(39) # You're a... teenager?
# Putting age >= 13 as the first statement means that any adult age
# causes the first statement to evaluate as True, so the "You are an adult"
# elif statement and string never triggers

def correct_status_checker(age):
    # Flipping the first two conditions:
    # Statements are now ordered from MOST to LEAST restrictive
    # Meaning if a statement is True, all the other statements that follow are
    # also True
    if age >= 18:
        return "You are an adult"
    elif age >= 13: 
        return "You are a teenager"
    elif age >= 4:
        return "You are a child"
    elif age >=2:
        return "You are a toddler"
    else:
        return "You are a baby"

# If a conditional logic statement is not behaving as expected
# you should always check that the conditions are ordered properly

correct_status_checker(1) # You are a baby!
correct_status_checker(3) # You're a toddler!
correct_status_checker(9) # You're a child!
correct_status_checker(14) # You're a teenager!
correct_status_checker(39) # You're an adult!

# What happens when you have multiple conditions that you want to check?

def can_legally_drink(country,age):
    # The answer depends on the country AND age
    # To do this, we nest if statements
    # First we pick one condition
    if country == "USA":
        # Then inside the block, we handle the other condition
        if age >= 21:
            return "You can legally drink in the USA"
        else:
            return "You cannot legally drink in the USA"
    elif country == "Canada":
        if age >= 19:
            return "You can legally drink in Canada"
        else:
            return "You cannot legally drink in Canada"
    if country == "France":
        if age >= 16:
            return "You can legally drink in France"
        else:
            return "You cannot legally drink in France"
    else:
        return "I don't know that country"

can_legally_drink("USA",22)
can_legally_drink("USA",13)
can_legally_drink("Canada", 19)
can_legally_drink("France", 15)

# Could we write this differently? Of course!

def can_legally_drink_with_and(country,age):
    if (country == "USA") and (age>=21):
        return "You can legally drink in the USA"
    if (country == "USA") and (age<21):
            return "You cannnot legally drink in the USA"
    if (country == "Canada") and (age>=19):
            return "You can legally drink in Canada"
    if (country == "Canada") and (age<19):
                return "You cannot legally drink in Canada"
    if (country == "France") and (age>=16):
                return "You can legally drink in France"
    if (country == "France") and (age<16):
                    return "You cannot legally drink in France"

# Nesting is slightly better because it doesn't check both conditions at once
# so it costs less runtime/compute

# When you have a simple condition, you can write a conditional logic block
# In a single line: that's called the "Ternary Operator"
age = 20
status = "Adult" if age >=18 else "Minor"
# VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE