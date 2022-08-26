#Write a Python program to remove duplicates from a list.

# using set in-built function
lst = input("enter the items: ")
lst = lst.split(",")
print(lst)

print(list(set(lst)))

