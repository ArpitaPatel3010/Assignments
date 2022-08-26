#Write a Python script to check if a given key already exists in a dictionary.
my_dict = {
'a':1,
'b':2,
'c':3
}
def checkey(key,my_dict):

    if key in my_dict.keys():
        print("present")
    else:
        print("not present")
key = 'v'
checkey(key, my_dict)
     