#How will you compare two lists?

list1 = []
data1 = int(input("how many nums of list1 : "))
for i in range(data1):
    lst1 = int(input("enter the nums of list1: "))
    list1.append(lst1)
    list1.sort()
print(list1)

list2 = []
data2 = int(input("how many nums of list2 : "))
for i in range(data2):
    lst2 = int(input("enter the numbers of list2: "))
    list2.append(lst2)
    list2.sort()
print(list2)

if list1 == list2:
    print("both are same list")
else:
    print("both are not same")