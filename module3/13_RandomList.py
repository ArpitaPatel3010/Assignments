#Write a Python program to select an item randomly from a list.
import random

list1 = []
list = int(input("total items to b inserted: "))
for i in range(list):
    items = input("enter item : ")
    list1.append(items)
print(list1)


ran_item = random.randrange(len(list1))
print(ran_item)