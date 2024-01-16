#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

print(f"Last digit of {number} is {number % 10}", end=" ")

if number % 10 == 0 and number != 0:
    print(f"and is 0")
elif number < 0:
    print(f"and is -{last_digit} and is less than 6 and not 0")
elif last_digit > 5:
    print("and is greater than 5")
else:
    print(f"and is less than 6 and not 0")
