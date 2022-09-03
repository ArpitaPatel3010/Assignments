#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
length = int(input("enter length: "))
width = int(input("enter width: ")) 

rec_obj = Rectangle(length,width)
result = rec_obj.area()
print("area of rectangle is",result)


        