#Write a Python program to convert a list of characters into a string.

#list = ['a','r','p','i','t','a']
lst = []
list = int(input("total elements to be inserted:"))
for i in range(list):
    data = input("enter char: ")
    lst.append(data)
print(lst)

a = ''.join(lst)
print(a)