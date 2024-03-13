'''Why we need OOP
Everything in Python is object
What is objects - 

'''

#CLASS
'''Class is a blueprint
Object belongs to a class
class  - 1.data or property or attributes
         2.functions or behaviour'''

a = 2
print(type(a)) #<class 'int'> a is object of integer class i.e here data type is class
#example
class Car: #class name pascal case ThisIsPascalCase
    #data
    color = 'blue' #snakecase this_is_snake_case
    model = 'sports'
    #method
    def calculateAvgSpeed(km,time): #snakecase this_is_snake_case
        #code
        pass

#Object - instance of class
        
WagonR = Car()

L = list()  #list class object
s = str() #string class object


#Function vs Methods
'''Method is special function written inside class, functions are normal and not 
inside any class'''

L = [1,2]

len(L) #function, not belong to any class,available for all,general
L.append(3) #method, function defined inside List class  

#CONSTRUCTOR __init__(self)
class Atm:
    '''__init__ is a special method in Python classes used for initializing newly created 
objects. It stands for "initialize" and is also known as the constructor method. 
When you create a new instance of a class (i.e., an object), 
Python automatically calls the __init__ method for that class.
Constructor is special method, which gets executed automatically 
when you create object of a class'''
'''IMP - no method in class can call another methods of the same class,
we can achieve this using object, and self refers to object that we are currently working 
with. So we have to pass self to every method.'''
    def __init__(self): #constructor name should always be init

        print("Constructor run hua")
        

sbi = Atm() # as soon as we run this, it will print 'Constructor run hua'



#DUNDER/MAGIC/SPECIAL methods
'''with double underscore like __init__
we can't call it with objects, they invoked automatically'''