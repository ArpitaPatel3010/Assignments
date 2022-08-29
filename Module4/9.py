#Write a Python program to count the frequency of words in a file.

file1 = open("file.txt","r")

dict = {}

for line in file1:
    line = line.strip()

    line = line.lower()

    words = line.split(" ")

    for word in words:
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] = 1

for key in list(dict.keys()):
    print(key, ':', dict[key])
