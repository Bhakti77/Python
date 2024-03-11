#COLLECTIONS module

#COUNTER
'''The Python Counter is a subclass of dictionary 
object which helps to count hashable objects.
A dictionary subclass that supports convenient counting of unique items in a sequence or iterable'''

from collections import Counter

a = 'aabbddjhsfjsdnmjskaldjalhdcbkagdssafdsvb'
print(Counter(a))
#Counter({'d': 7, 'a': 6, 's': 6, 'b': 4, 'j': 4, 'h': 2, 'f': 2, 'k': 2, 'l': 2, 'n': 1, 'm': 1, 'c': 1, 'g': 1, 'v': 1})

b = [1,2,4,6,56,5,64,5,3,43,2,31,31,12,12,1,2,12,12,1,2,12,4,4,4,3,4,3]
print(Counter(b))

c = (1,2,4,6,56,5,64,5,3,43,2,31,31,12,12,1,2,12,12,1,2,12,4,4,4,3,4,3)
print(Counter(c))

#NAMEDTUPLE
'''A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack. 
For example, consider a tuple names student where the first element represents fname, second represents lname
 and the third element represents the DOB. Suppose for calling fname instead of remembering the index position 
 you can actually call the element by using the fname argument, then it will be really easy for accessing 
 tuples element. This functionality is provided by the NamedTuple.'''
#It was used to eliminate the problem of remembering the index of each field of a tuple object in ordinary tuples.


from collections import namedtuple

# Define a namedtuple type called Point with two fields: x and y
Point = namedtuple('give_any_string_here', ['x', 'y'])

# Create a Point instance
p = Point(1, 2)

# Access the fields by name
print(p.x, p.y)  # Output: 1 2

Student = namedtuple('studentDetails',['fname','lname','age'])

s = Student('Bhakti','Padwal',26)

print(s.fname)

#ORDEREDDICT

'''OrderedDict is a dictionary subclass from the collections module that maintains the order of keys as they
 are added. In a regular dictionary, the order of keys is arbitrary and not guaranteed, 
while an OrderedDict remembers the order in which keys were inserted.'''

from collections import OrderedDict

od = OrderedDict()
od['banana'] = 1
od['apple'] = 2
od['cherry'] = 3

print(od)

d = dict()
d['banana'] = 1
d['apple'] = 2
d['cherry'] = 3

print(d)