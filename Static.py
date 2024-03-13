'''static
we have 2 types of variables,
instance variable whose value is diff for every object (they are inside constructor)
and sometimes we need a variable whose value is same for every object which is 
called as static/call variable((they are outside constructor))
like ifsc for all customers or school name for all students of that school'''


class Atm:
    counter = 1 #static variable,access using class name instead of object
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.sno = Atm.counter  
        Atm.counter = Atm.counter + 1
        #self.menu()

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
hdfc = Atm()
axis = Atm()

print(axis.sno)