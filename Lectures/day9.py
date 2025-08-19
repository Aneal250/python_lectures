#  Write a function that simulates rolling a pair of six sided dice. The function wil not
# take any parameters. It wil return the total that was rolled on two dice as its only
# result.
#
import random

def roll_dice():
    # Roll two dice
    die1 = random.randint(1, 6)  # first die
    die2 = random.randint(1, 6)  # second die

    total = die1 + die2
    return total


for i in range(5):
    result = roll_dice()
    print("Roll", i + 1, ":", result)