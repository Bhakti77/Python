'''Modules
In Python, a module is a file containing Python code. The code can define functions, 
classes, and variables that you can use in other Python files by importing the module.
Modules allow you to organize your Python code into reusable units, making your code more
modular and easier to maintain.'''

#help('modules')

#MATH module
import math
 
print(math.floor(20.6))
print(math.pi)
print(math.factorial(5))
print(math.floor(20.85))

#random module
import random

print(random.randint(1,10))
a = [1,2,3,4]
random.shuffle(a)
print(a)

#TIME Module
import time
print(time.time())

print(time.ctime())

print("hey")
#time.sleep(2)
print("you")

#OS module
import os

print(os.getcwd())

print(os.listdir())
