#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math
class circle():
    def __init__(self,radius ):
        self.radius = radius
        
    def perimeter(self):
        return math.pi *self.radius*2

    def area(self):
        return math.pi*(self.radius**2)

radius_input = int(input("enter radius: ")) 
    
peri_obj = circle(radius_input)
result = (peri_obj.perimeter())
result2 = (peri_obj.area())

print("Perimeter of circle is: ",result)
print("Area of circle is: ",result2)