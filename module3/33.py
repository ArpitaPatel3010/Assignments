#Write a Python script to concatenate following dictionaries to create a new one.
dic_1={'a': 1,
       'b': 2}

dic_2={'c':3,
        'd':4}

dic = {}

for d in (dic_1,dic_2) : dic.update(d)
print(dic)