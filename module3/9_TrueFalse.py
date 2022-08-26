# Write a Python function that takes two lists and returns true if they have 
# at least one common member.

# lst1 = [1,2,3,4]
# lst2 = [4,5,6,7]



def common(lst1,lst2):
    result = False
    for i in lst1:
        for j in lst2:
            if i == j:
                result = True
                return result
    return result

lst1 = input("enter num: ")
lst1 = lst1.split(",")
#print(lst1)

lst2 = input("enter num: ")
lst2 = lst2.split(",")
#print(lst2)

print(common(lst1,lst2))

      
