'''Python Lists are just like dynamically sized arrays, 
declared in other languages (vector in C++ and ArrayList in Java). 
In simple language, a list is a collection of things, enclosed in
 [ ] and separated by commas. '''

#List vs arrays
#Arrays contain elemetns with same data type,lists can contain diff data types
#Lists are dev friendly, arrays are faster due to how they get stored in memory
#Lists are mutable, we can edit the list

#empty list
my_list = []
print (my_list)

L = list()
print(L) #[]

#homo
my_list2 = [1,2,3,4,5,6]
print(my_list2)

#hetero
my_list3 = ['Bhakti',1,2,3,4,True,5.023,(5+6j)]
print(my_list3)

#multidimensional
my_list4 = [[1,2],[3,4],[5,6],[7,8]]
print(my_list4)

my_list5 = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(my_list5)

#converting string to list
str = list("Bhakti")
print(str) #['B', 'h', 'a', 'k', 't', 'i']

#Accessing list elements
print(my_list3[0])
print(my_list4[0])
print(my_list4[0][1])
print(my_list5[0])
print(my_list5[1][0])
print(my_list5[1][0][0]) #5
print(my_list2[-1],my_list2[-2]) #last element and second last

#Editing the list
print(my_list2)
my_list2[0] = 8
print(my_list2)

my_list2[-1] = 66
print(my_list2)

#add
#append
#append will always add only one value
my_list2.append('Bhakti')
print(my_list2)
my_list2.append([5,6]) #[8, 2, 3, 4, 5, 66, 'Bhakti', [5, 6]]
print(my_list2)

#extend
'''The extend() method expects an iterable (like a list, tuple, set, etc.)
as its argument, not a single value. If you want to add a single value to the end of a 
list,you should use the append() method instead.'''
my_list2.extend([85,85.6354,'Japan'])
print(my_list2)

#if we give string, it will get converted into list first 
my_list2.extend("goa")
print(my_list2) 
#[8, 2, 3, 4, 5, 66, 'Bhakti', [5, 6], 85, 85.6354, 'Japan', 'g', 'o', 'a']


#Insert list.insert(index,value)
print(my_list3)
my_list3.insert(1,"Hey")
print(my_list3)
my_list3.insert(0,[2,58])
print(my_list3)

#delete
#del,remove,pop,clear

print(my_list2)
#[8, 2, 3, 4, 5, 66, 'Bhakti', [5, 6], 85, 85.6354, 'Japan', 'g', 'o', 'a']

del[my_list2[-1]]
print(my_list2)

del[my_list2[-2:]]
print(my_list2)

#remove(value)
my_list2.remove(66)
print(my_list2)

#pop will delete last element
my_list2.pop()
print(my_list2)

#clear - empty the list
my_list2.clear()
print(my_list2) #[]

#operations with list
l1 = [1,2,3,4]
l2 = [5,6,7,8]

print(l1+l2) #[1, 2, 3, 4, 5, 6, 7, 8] concatenation
print(l1*3) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

#loop
for i in l1:
    print(i)

#in
print(4 in l1) #True
print('n' in l2) #False

#Functions in list
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l2,reverse=True)) #not permanent op , will craete new list
l1.sort(reverse=True) #permanent op , will work on existing list
print(l1)
print(l1.index(2)) #index of 2 in l1

print(("bhakti japan").title()) #first letter capital Bhakti Japan

#que convert first letter to capital
def title1(str):
    l  = []
    for i in str.split(' '):
        #print(i.capitalize())
        l.append(i.capitalize())
    return l

op = title1("how are you")
print(op) #['How', 'Are', 'You']
print(" ".join(op)) #How Are You
#que 
email = 'bhaktigmail.com'
if email.find("@") == -1:
    print("character not found,try different char")
else:
    print(email[:email.find("@")])