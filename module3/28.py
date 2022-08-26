#Write a Python program to remove an empty tuple(s) from a list of tuples.

tup = [(),(1,2,3),(),(4,5,6)]

for i in tup:
    if len(i) == 0:
        tup.remove(i)
print(tup) 

# for i in tup:
#     print(len(i))