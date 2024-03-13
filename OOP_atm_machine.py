class Atm:
    '''__init__ is a special method in Python classes used for initializing newly created 
objects. It stands for "initialize" and is also known as the constructor method. 
When you create a new instance of a class (i.e., an object), 
Python automatically calls the __init__ method for that class.
Constructor is special method, which gets executed automatically 
when you create object of a class'''
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        print("1.Create pin")
        print("2.Deposit")
        print("3.Withdraw")  
        print("4.Check balance")
        user_input = int(input("Choose from the below"))
        if user_input == 1:
            self.CreatePin()
        if user_input == 2:
            self.Deposit()
        if user_input == 3:
            self.Withdraw()
        if user_input == 4:
            self.CheckBalance
        else:
            print("Bye")

    def CreatePin(self):
        self.pin = int(input("Enter the pin"))
        print("Pin set successfully")
    
    def Deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")

    def Withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance - amount
            print("Withdraw successful")
        else:
            print("Invalid pin")

    def CheckBalance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")


sbi = Atm()