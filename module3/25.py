#Write a Python program to reverse a tuple.

# def Reverse(tuples):
#     new_tup = tuples[::-1]
#     return new_tup

# tuples(1,2,3,4)
# print(Reverse(tuples))

# OR


tup = (input("enter tup: "))
print(tup)
new_tup = tuple(reversed(tup))
print(new_tup)