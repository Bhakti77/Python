'''Inheritance - is a relationship
e.g parent - child'''

#what we inherit - variables,methods,constructor

#private members are not inherited

class User:

    def login(self):
        print("Log in")

    def register(self):
        print("register")

class Student (User):    #extending User class, Stduent is subclass of User 
  
    def enroll(self):
        print("enroll")
    
    def review(self):
        print("review")

s1 = Student()

#Student is accessing User methods as well because of inheritance,but User class cannot access methods of Student class
s1.login()
s1.enroll()
s1.register()
s1.review()

#ANOTHER EXAMPLE
class Phone:

    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

    def buy(self):
        print("Buy phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buy smartphone")

#if child class is not having any constructor, then parent constructor will be called
s = SmartPhone(20000,'Apple',13) #op - Inside phone constructor

#private members are not inherited
#print(s.__brand) #op - 'SmartPhone' object has no attribute '__brand'

s.buy()