#Write a Python script to merge two Python dictionaries
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
dic = {}
dic_3 = {}
new_dic={}
#Using | operator
print(dict_1 | dict_2)

# Using update()
dic  = dict_2.copy()
dic.update(dict_1)
print(dic_3)

new_dic=dic.update(dic_3)
print(new_dic)