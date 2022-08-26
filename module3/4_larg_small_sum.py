# Write a Python function to get the largest number, smallest num and sum 
# of all from a list.



list = []
data = int(input("enter the nubers inserted: "))
for i in range(data):
    lst = int(input("enter the nums: "))
    list.append(lst)
print(list) 

#to get the largest num from the list
l_num = max(list)
print("largest num is:",l_num)

#to get the smallest num
s_num = min(list)
print("smallest num is: ", s_num)

#to get the sum of all nums
sum_num = sum(list)
print("sum is: ",sum_num)