#Write a Python program to write a list to a file.

name = ['hello','world']
file1 = open("file.txt",'w+')

for items in name:
    WriteList = file1.write(items)
print(WriteList)

file1.close()