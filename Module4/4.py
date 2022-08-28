#Write a Python program to read first n lines of a file.

#input the text file
InputFile = "file.txt"

#Enter the N lines of file you want to see
N  = int(input("Enter N values: "))

#reading a file /file opening in a read mode
file1 = open(InputFile,"r")
line_list = file1.readlines()
print(line_list)

print("The",N,"lines are")

#Travaersing the line list
for txt in (line_list[:N]):
    print(txt)
    