# Write a Python function that takes a list and returns a new list with unique 
# elements of the first list

def unique_list(lst1):
    lst2 = []
    for i in lst1:
        if i not in lst2:
            lst2.append(i)
    return lst2

lst1 = input("enter the items : ")
new_list = lst1.split(",")
print("list: ",new_list)
print("list with unique Elements",unique_list(new_list))

