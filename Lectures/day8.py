# iterations
# Assignment Operators
# priming Read
# Terms 
# a) header
# b) block
# c) return
# d) parameter

# Types of Variable
# a) global
# b) constant
# c) defined
# d) local

# a) Filename
# b) Extension
# c) File object
# d) File variable

# b) random


# iterations
# meaning or mapping through something, 
# data type list = [1, 2, 3, 4, 5] # iterate through these

artist  = [ 'davido', 'wizkid', 'burna boy', 'tems', 'olamide']
# for loop,
for i in artist:
    print(f'hello Artist  {i}')

# print number from 1 to 10
# range(stop)
# range(start, stop)
# range(start, stop, step)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 11):
    print(f'hello Number  {i}')



 # Assignment Operators   
# example  =, +=, -=, *=, /=, //=, %=, **=
name = "sandra_bae"
x = 5
x += 2  # x = x + 2


# priming Read
# it a technique used in loops when reading input.
number = int(input("Enter a number: "))  # priming read


# a) header
# the first line of a function or method definition
#write a function to add two numbers

def add_numbers(a, b): # parameters
    return a + b

print(add_numbers(5, 10))  # Output: 15 #arguements
print(add_numbers(31, 21))  


# b) block
# it a group of statement inside a function

age = 21
if  age >= 18:
    print("you can watch 18+ movies")


 # c) return
 # it is used to return a value from a function   


 # d) parameter
 # they are placeholder variable inside a function definitions

# example
def greet(name): # parameters
    return f"Hello, {name}!"


# Types of Variable
# a) global
# b) constant
# c) defined
# d) local

x = "students" # global variable

def greet(name): 
    return f"Hello, {name}!"

def hello():
    global x  # access the global variable
    return f"Hello, {x}!"


# a) Filename. #day8.py
# b) Extension. .py
# c) File object
# d) File variable

# b) random
# and unpredictable value
