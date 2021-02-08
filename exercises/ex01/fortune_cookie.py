"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730287108"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = randint(1, 4)
if fortune < 3:
    if fortune < 2:
        print("You will adopt a long-haired cat named Tom.")
    else:
        print("You will meet the love of your life this year.")
else:
    if fortune < 4:
        print("You will enjoy a large chocolate chip cookie with icecream soon.")
    else:
        print("You will read an inspring book this month.")
print("Now, go spread positive vibes!")