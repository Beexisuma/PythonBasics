# Why Python?
# Python is a popular choice for programming due to its simplicity, readability, and extensive libraries.
# Its versatility spans web development, data science, machine learning, and more.
# Python's supportive community, cross-platform compatibility, and in-demand skills
# make it an excellent language for both beginners and experienced developers.

# Basic Print Statement
print("Hello World!")

# "Hello World!" is defined as a 'string', as it is in quotes
# There are also variables, integers, and floats
# A variable can be a string, an integer, or a float
# Imagine a variable is the umbrella, and the other 3 terms fall below it
# An integer is any whole number
# A float is any number with a decimal

# Demonstrating a string
print("Hello World!" * 2)

# print("Hello World!" + 2)
# The above line will return an error, as you cannot add 2 to a sentence

# Demonstrating an integer
print(4 * 2)

# Demonstrating a float
print(4.3 * 2.0)

# Variable Definition
# Defining clear and concise variables is important -
# without this, you may lose track of what variables mean what,
# or you may have to type out long names every time you want to use one.
# variables may not contain spaces, underscores are a common replacement
sum_of_nums = 1+2
print(sum_of_nums)

# Concatenation - also known as combining terms
intro = "The sum of the numbers is: "
print(intro, sum_of_nums)

# Use '#' to comment out one line of code at a time.
# This means that the computer cannot see this line and will not attempt to execute it.
# This is useful for writing notes in your code

# While Statements
# one = 1
# while one == 1:
#     print("Repeated Statement")

# Ending a while statement
# one = 1
# while one == 1:
#     print("Repeated Statement")
#     one = 2

# For Loops
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(number)

# The built-in 'len' function will output the amount of items in the list
print("The length of the list is: ", len(number_list))

# Remember, the list starts at 0, rather than one.
# This means that the first item in the list is the number 0.
# In this example, that means printing the number_list of [0] would output the number 1
print(number_list[0])

# If, Else Statements
# When defining a variable, use '='
# When comparing, use '=='

# This statement will print 'True!'
one = "this statement is true"
if one == "this statement is true":
    print("True!")
else:
    print("False!")

# This statement will print 'False!'
one = "this statement is not true"
if one == "this statement is true":
    print("True!")
else:
    print("False!")

# Lastly, let's look at user input
user_input = input("Enter a number: ")
print(user_input)
# The below line will not be executed until the user has inputted a number
print("Goodbye!")

# Please try some of these exercises yourself, and good luck!
