

import os

# * file detection

path = "C:\\Users\\freed\\Desktop\\test1.txt"

if os.path.exists(path):
    print("that location exists!")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("that location dosn't exist")



# * file reading in python

try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
# print(file.closed)


# * file writing in python


text = "prova scrittura\n prova scrittura test"

# 'r' for reading
# 'w' for overwriting
# 'a' for append / writing after what's already written 

with open('text.txt', 'a')as file:
    file.write(text)