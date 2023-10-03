#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10 if number > 0 else -(abs(number) % 10)
print(f"Last digit of {number:d} is {ldigit:d} ", end="")

if ldigit > 5:
    print(f"and is greater than 5")
elif not ldigit:
    print(f"and is 0")
elif ldigit < 6 and ldigit:
    print(f"and is less than 6 and not 0")
