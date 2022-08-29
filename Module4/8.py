#Write a Python program to count the number of lines in a text file.

file1 = open("file.txt", 'r') 

lines = len(file1.readlines())

print('Total Number of lines:', lines)