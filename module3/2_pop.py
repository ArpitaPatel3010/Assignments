#2. How will you remove last object from a list?

list = []
num = int(input("enter number you want: "))
for i in range(num):
    list1 = input("enter number: ")
    list.append(list1)
print(list)
list.pop()
print(list)