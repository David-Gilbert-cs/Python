'''
author : David Gilbert
Problem  : read/write from/to file

'''

#
# Read from file
#

#read the whole file and store it as a big string in text variable
with open('file_to_read.txt', 'r') as open_file:
    text = open_file.read()


#read line by line
with open('file_to_read.txt', 'r') as open_file:
    line = open_file.readchar()
    while line:
        print(line)
        line = open_file.readline()


#read line by line
with open('file_to_read.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = open_file.readline()
    
#   
# Write to File    
#


# 'w' overwrites the file  // 'a' appends
with open('file_to_save.txt', 'a') as open_file:
    open_file.write('A string to write')