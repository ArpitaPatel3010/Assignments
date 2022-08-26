#Write a Python program to find the second smallest number in a list.

lst = input("enter the items : ")
new_lst = lst.split(",")
new_lst.sort()

print("list: ",new_lst)
print("second smallest number is: ",new_lst[1])