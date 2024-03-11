'''Error in Python can be of two types i.e. Syntax errors and Exceptions. 
Errors are problems in a program due to which the program will stop the execution. 
On the other hand, exceptions are raised when some internal events occur which change 
the normal flow of the program.'''

#stacktrace
'''error or exception we see after we run the program.Stack traces are often displayed 
when an error occurs, helping you identify the source of the error in your code.'''


#compilation - syntax error
#print "Hello"; #not written according to program grammar
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello")?#
#error raised by interpreter/compiler

#types
#indentationerror
#modulenotfounderror
#keyerror in dictionary
#typeerror
#nameerror
#valueerror
#attributeerror
#indexerror
#filenotfounderror

#Execution - exceptions (logical error)

#TRY EXCEPT block
def create_file(file_path):
    try:
        with open(file_path,'w')as file1: #w create new file if not exists
            file1.write("try except practice")
            print("File created successfully")
            #print(m)
            print(5/5)
            l = [1,2,3]
            print(l[20])
    except FileNotFoundError:
        print("File not found")
    except NameError:
        print("Variable not defined")
    except ZeroDivisionError:
        print("Can't divide by zero")
        '''#this is generic exception, 
        #if we are not handling any error in except above,
        we should write a generic exception to find errors which we have not handled
        and it should be at last'''
    except Exception as e: 
        print(e.with_traceback) 

filepath = 'C:/Users/bhakt/OneDrive/Desktop/Python/file1.txt'

create_file(filepath)


#ELSE block
'''if there is no exception and try executed successfully, 
write code in else to be executed after try. If except occurs, else will not work''' 
try:
    with open('C:/Users/bhakt/OneDrive/Desktop/Python/file2.txt','w') as file2:#w create new file if not exists
        file2.write("try except and else practice")
        print("File created successfully")
except IOError:
    print("File could not be created")
else:
    print("All good")

#FINALLY block
'''It will execute no matter what exception or no exception
mostly we can use to close the file or any connection'''

try:
    with open('C:/Users/bhakt/OneDrive/Desktop/Pytho/file2.txt','w') as file2:#w create new file if not exists
        file2.write("try except and else practice")
        print("File created successfully")
except IOError:
    print("File could not be created")
else:
    print("All good")
finally:
    print("In finally block")


#RAISE EXCEPTION, like THROW in JAVA
'''Exceptions are raised as error occured at runtime
We can also manually raise exceptions using raise keyword
We can optionally pass the value to exception to clarify why that exception was raised'''

def withdraw(amount):
    balance = 10000
    if amount < 0:
        raise Exception ("Amount cannot be negative")
    if amount > balance:
        raise Exception ("Amount cannot be greater than balance")
    balance = balance - amount
    return balance
    
try:
    op = withdraw(30000)
except Exception as e: #this e is object thrown/raised above
    print(e)
else:
    print(op)
finally:
    print("Done")

#CREATING CUSTOM EXCEPTIONS
'''why to create custom exceptions?
when we need extra addition as per our requirement and do not need simple messages'''
class MyOwnException(Exception):
    def __init__(self, message):
        print(message)

def withdraw(amount):
    balance = 10000
    if amount < 0:
        raise MyOwnException("Amount cannot be negative")
    if amount > balance:
        raise MyOwnException("Amount cannot be greater than balance")
    balance = balance - amount
    return balance
    
try:
    op = withdraw(30000)
except MyOwnException as e: #this e is object thrown/raised above
    pass
else:
    print(op)
finally:
    print("Done")