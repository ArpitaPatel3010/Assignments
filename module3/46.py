#Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': #400}, {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}]

test_list = [{'bad': [1, 5, 6, 7], 'good': [9, 6, 2, 10],
              'CS': [4, 5, 6]},
             {'bad': [5, 6, 7, 8], 'CS': [5, 7, 10]},
             {'bad': [7, 5], 'best': [5, 7]}]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Concatenate Similar Key values
# Using loop
res = dict()
for dict in test_list:
    for list in dict:
        if list in res:
            res[list] += (dict[list])
        else:
            res[list] = dict[list]
 
# printing result
print("The concatenated dictionary : " + str(res))