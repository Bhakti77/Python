#Datatypes
# Numeric --- Integer float complex   
a = 5
print("Type of a: ", type(a)) 
  
b = 5.0
print("\nType of b:    ", type(b)) 
  
c = 2 + 4j
print("\nType of c: ", type(c)) 

#Sequence Data Type in Python
#String, list,tuple
String1 = 'Welcome to the Geeks World'
print("strings with the use of Single Quotes: ") 
print(String1) 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes : ") 
print(String1) 
print(type(String1)) 

String2 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String2) 
print(type(String2)) 
  
String3 = '''Geeks  
            For  
            Life'''
print("\nCreating a multiline String: ") 
print(String3) 

#Creating a List in Python
#Lists in Python can be created by just placing the sequence inside the square brackets[]. 

List = [] 
print("Initial blank List: ") 
print(List) 
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0]) 
print(List[2]) 
List = [['Geeks', 'For'], ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 


#Creating a Tuple in Python
'''In Python, tuples are created by placing a sequence of values separated by a ‘comma’ 
with or without the use of parentheses for grouping the data sequence. 
Tuples can contain any number of elements and of any datatype 
(like strings, integers, lists, etc.). 
Note: Tuples can also be created with a single element, but it is a bit tricky. 
Having one element in the parentheses is not sufficient, 
there must be a trailing ‘comma’ to make it a tuple.'''

Tuple1 = () 
print("Initial empty Tuple: ") 
print(Tuple1) 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 
tuple4 = (1,) #without comma, it will be int
print(tuple4)
print(type(tuple4))

#Boolean Data Type in Python
print(True)
print(False)
print(type(True))

#Set Data Type in Python
set1 = {1,2}
print(set1)
print(type(set1))

set2 = set() #empty set 
print(set2)
print(type(set2))

#Dictionary Data Type in Python

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 
