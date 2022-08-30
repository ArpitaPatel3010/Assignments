#Write a Python program to copy the contents of a file to another file.
 
file1 = open("file.txt",'r')
file2 = open("new_file.txt",'a')

for words in file1:
     a = file2.write(words)
print(a)