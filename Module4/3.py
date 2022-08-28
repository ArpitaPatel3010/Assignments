#Write a Python program to append text to a file and display the text.

file1  = open("file.txt",'w')
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.close()

#appending a text / it adds at the end 
file1 = open("file.txt","a")
file1.write("Today\n")
file1.close()

file1 = open("file.txt","r")
print("output of a file after appending is")
print(file1.read())
