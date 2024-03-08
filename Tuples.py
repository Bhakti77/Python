'''Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.'''
#tuples are read-only data type

#empty
tuple1 = ()
print(tuple1)

tuple2 = (1,2,4,5,3,4,5,6,7,8,9)
print(tuple2)

tuple3 = (1,2,'Hey',"Japan",'Bhakti',45.23,True)
print(tuple3)

tuple4 = ((1,2),(2,3))
print(tuple4)

#imp, tuple with 1 element, you have to give comma otherwiese it will be integer
t1 = (1) #int
t2 = (1,) #tuple
print(t2)

#access tuple items, same as list
print(tuple2[3]) #5

#we cannnot edit tuples as they are immutable,no add no insert no append
#tuple2[0] = 3
#error 'tuple' object does not support item assignment

#delete
#del tuple2[0]
#error 'tuple' object doesn't support item deletion
#as deleting 1 item will change the tuple, it's not allowed

#operation with tuple
t3 = (1,2,3,4)
t4 = (5,6,7,8)

print(t3+t4) #(1, 2, 3, 4, 5, 6, 7, 8) concatenation
print(t3*3) #(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

#loop
for i in t3:
    print(i)

#in
print(4 in t3) #True
print('n' in t4) #False

#Functions in tuple
print(len(t3))
print(min(t3))
print(max(t3))
print(sorted(t3,reverse=True)) #not permanent op , will create new list
print(t3)
print(t3.index(2))