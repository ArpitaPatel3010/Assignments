#Write a Python script to sort (ascending and descending) a dictionary by value.
from optparse import Values


my_dict = {'a': 2,
           'c': 1,
           'b': 3}


sorted_items = sorted([(key, value)
for (key, value) in my_dict.items()])

print(sorted_items)
  