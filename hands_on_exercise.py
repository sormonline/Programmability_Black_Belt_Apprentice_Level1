"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("value of pi is {}. type is {}.".format(pi, type(pi)))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50 or i >50:
    print(i)


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'banana':
    print("yellow")
elif picked_fruit == 'strawberry':
    print("red")
else:
    print("orange")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplie(n1, n2):
    return n1*n2

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", multiplie(12, 96))

print("48 x 17 =", multiplie(48, 17))

print("196523 x 87323 =", multiplie(196523, 87323))
