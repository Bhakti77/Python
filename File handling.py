'''Python supports file handling and allows users to handle files 
i.e., to read and write files, along with many other file handling options,
to operate on files.'''
''' sequence of characters, and they form a text file. 
Each line of a file is terminated with a special character, called the EOL or 
End of Line characters like comma {,} or newline character. 
It ends the current line and tells the interpreter a new one has begun.'''

#Python file open
file_path = "C:/Users/bhakt/OneDrive/Desktop/Python/geeks.txt"
file = open(file_path,'w+')
for eachline in file:
    print(eachline) 
file.write("Hey there\n")
file.write("You are overriding\n")
file.write("It allows us to write in a particular file")
print("done")

#Using with Statement: It's a good practice to use the with statement to open a file. 
#It automatically closes the file when the block is exited, even if an exception occurs.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
'''Where the following mode is supported:
r: open an existing file for a read operation.
w: open an existing file for a write operation. 
If the file already contains some data, then it will be overridden 
but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.#'''

filepath = "C:/Users/bhakt/OneDrive/Desktop/Python/file1.txt"
def create_file(file_path):
    try:
        file1 = open(file_path,'w') #w create new file if not exists
        file1.write("Hello World,\nexperience new world")
        print("File created successfully")
    except IOError:
        print("Error:could not create file")

def read_file(file_path):
    try:
        file = open(file_path,'r')
        line = file.read()
        print(line)
    except IOError:
        print("Error:could not read file")


def append_text_to_file(file_path,text):
    try:
        file = open(file_path,'a')
        file.write(text)
        print("Appened successfully")
    except:
        print("Error:could not append to file")


create_file(filepath)
read_file(filepath)
append_text_to_file(filepath,"\n Bhakti Padwal")