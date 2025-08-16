# Preparation 
#  Read the 🍥 

# Next to work on 
# Inheritance
# operators
# conditions, 
#  library functions
# go through these concepts
# a) modifier
# b) constructor
# c) mutator
# d) accessor
# the difference between __int__ method and __str__ method


#Definition

# Inheritance: a process where child gets sometime from parent.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Bark



# operator
# Operators are special symbols that perform operations on variables and values.

#Types of operators
#. 1. Arithmetic Operators (focus)
# 2. Relational Operators (focus)
# 3. Logical Operators (focus)
# 4. Assignment Operators
# 5. Bitwise Operators
# 6. Identity Operators
# 7. Membership Operators

# #. 1. Arithmetic Operators (focus)
# example  +, -, *, /, //, % , **
sum = 2 + 3
print(sum)


# 2. Relational Operators (focus)
# example  ==, !=, >, <, >=, <=
a = 5
b = 10
c = 5
print(a < b) # 

print(a == c ) # True

print(a != c) # False

print (b >= a) # True


# 3. Logical Operators (focus)
# example  and, or, not

sandra = {
    "name" : "Sandra",
    "age" : 21,
    "is_student" : True,
    "sex" : "Female"
}

emmanuel = {
    "name" : "Emmanuel",
    "age" : 18,
    "is_student" : False,
    "sex" : "Male"
}

monthly_stipend = "$500"

isqualified = sandra["is_student"] and emmanuel["is_student"]  # both condition must true

print(f"Result: {isqualified}")  # Output: False

isqualifiedCar = sandra["is_student"] or emmanuel["is_student"]  # at least one condition must be true


isqualifiedMarrige = not sandra["is_student"]  # negates the condition. // opposite of the condtions.


# conditions, 

# example if, elif, else

age = 18
if age >= 18:
    print("You can have BoyFriend")
elif age < 18 and age >= 16:
    print("You can have BoyFriend")
else:
    print("You cannot have BoyFriend")


#  library functions (Methods)

name = "Sandra" 

print(name.upper())  # Output: SANDRA
print(name.lower())  # Output: sandra
print(name.title())  # Output: Sandra



# a) modifier (setter method)
# A methods that change the value of the object

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount): #modifier
        self._balance += amount



# c) mutator
    def withdraw(self, amount): #mutator
        self._balance -= amount


# b) constructor
 # They are methods that always run at the beginning of the object lifecycle.

# it a special method that runs automatically when an object is created.

# example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



# Accessor (getter Method)
    def get_balance(self):
        return self._balance


# the difference between __int__ method and __str__ method in class

#__init_ method
#1. contructor
#2. called when the object is created.
#3. used to initialize the attributes of the object.


#__str__ method
#1. used to define a string representation of the object.
#2. called when the object is converted to a string (e.g., using print).
#3. should return a human-readable string describing the object.