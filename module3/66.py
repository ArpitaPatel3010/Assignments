#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers
#from decimal import *
data = input("enter elements you want to enter: ")
new_data = data.split(",")
print(new_data)

print("Maximum: ", max(new_data))
print("Minimum: ", min(new_data))