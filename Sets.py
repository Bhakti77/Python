'''Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets.'''

#sets does not allow duplicated
#no indexing, so no slicing
#sets does not allow mutable data types
#sets itself is mutable, we cannot have multidimensional sets.

#empty
set1 = {}
print(set1)
print(type(set1)) #class dict

set2 = set()
print(set2) #set

s3 = {1,2,4,5,6,7,8,9,4,5,3,2} #it will not print duplicates {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s3)

s4 = {"Hello",4.5,6533,True}
print(s4)

#s5 = {[1,2,4,4],4} #it will throw error as list is mutable which is not allowed in sets
#print(s5)

s6 = {(1,2,4,4),4} ##it will work as tuple is immutable which is allowed in sets
print(s6)

print(s6[0]) #TypeError: 'set' object is not subscriptable

s7 = {{1,2},{3,4}} #not allowed
print(s7)
