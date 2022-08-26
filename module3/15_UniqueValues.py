#Write a Python program to get unique values from a list

def unique_value(lst1):
    lst2 = []
    for i in lst1:
        if i not in lst2:
            lst2.append(i)
    return lst2

lst1 = input("enter the items : ")
new_list = lst1.split(",")
print("list: ",new_list)
print("list with unique Elements",unique_value(new_list))
