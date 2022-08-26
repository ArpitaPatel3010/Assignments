#How Do You Check The Presence Of A Key In A Dictionary?
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
     