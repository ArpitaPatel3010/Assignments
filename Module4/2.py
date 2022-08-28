#Write a Python program to read an entire text file.

file1  = open("file.txt",'w')
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

# to write/ add new lines
file1.write("hello\n")
file1.writelines(L)
file1.close()

#Reads a file 
file1 = open("file.txt","r")

print("output of function is ")
print(file1.read())