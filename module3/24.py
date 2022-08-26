#Write a Python program to convert a list to a tuple.

lst = input("enter items: ")
lst1 = lst.split(",")
print("List: ",lst1)

tup = tuple(lst1)
print("list coverted to tuple: ",tup)
print(type(tup))
