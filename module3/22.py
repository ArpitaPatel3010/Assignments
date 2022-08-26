#Write a Python program to check whether an element exists within a tuple


tup = tuple(input("enter tuple: "))
print(tup)

a = input("enter the element to be searched: ")
if a in tup:
    print(True)
else:
    print(False)