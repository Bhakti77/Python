#for loop
'''A for loop is used for iterating over a sequence
 (that is either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

#range function
'''the range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.'''
#range(start(default 0),stop,step(optional))
for i in range(6): #excluded 6, 0 to 5
    print(i)

for i in range(1,7):
    print(i)

for i in range(0,6,2):
    print(i)

for char in 'Bhakti':
    print(char)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

