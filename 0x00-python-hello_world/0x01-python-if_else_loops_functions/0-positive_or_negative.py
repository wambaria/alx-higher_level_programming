#!/usr/bin/python3
import random
number = random.randint(-10, 10)
x = int(input("Enter a number: "))
if x > 0:
    print("positive")
elif x == 0:
    print("is zero")
else x < 0:
    print("negative")
