'''Encapsulation is the concept of restricting access to certain parts of an object.
You can use private variables and methods by prefixing them with double underscores __.'
We don't have Private keyword in Python'''

class Atm:

    def __init__(self):
        self.__pin = "" #private
        self.__balance = 0  #private

    '''Internally variables will be _Atm__pin,_Atm__balance (_classname__attributename)
it will create new variable __balance, which will not affect original one but
if u try to access using _Atm__pin,_Atm__balance, then it will change value of original,
so in Python nothing is actually private'''

    def __menu(self): #private
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
            self.CheckBalance()
        else:
            print("Bye")

    #getter and setter for accessing private variables
    def get(self):
        return self.__pin

    def set(self,new_pin):
        self.__pin = new_pin
        print("Pin changed")

sbi = Atm()
pin = sbi.get()
print(pin)