#  Write a python program to print the contents of a directory using the os module. Search online for the function which does that

import os

# Specify the directory you want to list out
directory_path = '/Windows'

# Get the contents of the current directory
contents = os.listdir(directory_path)

# Print each item
for item in contents:
    print(item)
