# Write a python program to find the longest words
def longestword(filename):

    file1 = open("file.txt","r")
    

    max_len = max(file.split(), key = len)
    print("longest word is: ", max_len)