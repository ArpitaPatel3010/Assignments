#Write python program that user to enter only odd numbers, else will raise an exception.

num = int(input("enter num: "))
data = num % 2
try:
    data>0
    print("This is odd num")
except ValueError:
    print("Enter odd num")
