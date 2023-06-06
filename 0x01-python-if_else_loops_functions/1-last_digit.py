#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    Lastdigit = number % 10
else:
    Lastdigit = number % -10

print("Last digit of", number, "is", Lastdigit, end=" ")

    if Lastdigit > 5:
    print("and is greater than 5")
elif Lastdigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
