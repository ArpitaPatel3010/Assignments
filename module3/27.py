#Write a Python program to find the repeated items of a tuple

tup = tuple(input("Enter elements: "))
var = int(input("enter num you want to find: "))
a = list(tup)
for i in range(len(a)):
    a[i] = int(a[i])
count = a.count(var)
print(var,"is repeated" ,count," time in a tuple")

# var=int(input())
# tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)  
# a=list(tup)
# for i in range(len(a)):
#   a[i]=int(a[i])
# count=a.count(var)
# print(var,'appears',count,'times in the tuple')

