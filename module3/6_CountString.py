# Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given 
# list of strings.

list = input("enter the items: ")
list = list.split(",")

print(list)

s=0
for i in list:
    if len(i)>2 and i[0] == i[-1]:
        print("The given string  are: ",i)
        s = s+1

print("total string is: ",s)