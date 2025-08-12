# functions

#  what are functions
#  Functions are reusable blocks of code that perform a specific task. They allow you to organize your code into logical sections, making it easier to read, maintain, and debug. Functions can take inputs (called parameters) and can return outputs (called return values). By using functions, you can avoid code duplication and improve the overall structure of your programs.


# def greet(name):
#     return f"Hello Goody, {name}!"

# emekaGreet = greet("Emeka")
# sandraGreet = greet("Sandra")

# print(emekaGreet)
# print(sandraGreet)

# // write function to calculate the area of a rectangle

# length * width
def calculateArea(length, width):
    return length * width


AreaTv = calculateArea(5, 30)

# print(AreaTv)


# // function to calculate the age difference between two siblings

def calculateAgeDifference(senior, junior):
    return senior - junior

sandraFamily = calculateAgeDifference(21, 18)    

anealsFamily = calculateAgeDifference(34, 31)


print(sandraFamily)
print(anealsFamily)


class Account:
    def __init__(self, accountNumber):
        self.accountNumber = accountNumber

        def get_balance(self):
            return self.balance



accounte = Account