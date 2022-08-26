#Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.


# lst = []
# for i in range(1,31):
#     lst = lst + [ i**2 ]
    
# print(lst[:5])
# print(lst[-5:])

lst =[]
lst1 =[]
for i in range(1,31):
    # lst = i
    # print(lst,end=" ")
    lst = i**2
    lst1.append(lst)

print("Square of 1st 5 elements of list: ",lst1[:5])
print("Square of last 5 elemnts of list: ",lst1[-5:])

