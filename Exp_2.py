class Rectangle:
    def __init__(self):
        self.le = int(input("Enter length"))
        self.be = int(input("Enter breadth"))
        self.r=int(input("Enter Radius"))
        self.h=int(input("Enter height"))
        self.b=int(input("Enter base"))
    def area(self):
        print(self.le * self.be)
    def peri(self):
        print(2 * (self.le + self.be))
class Circle(Rectangle):
    def area(self):
        super(Circle, self).area()
        print(3.14*self.r*self.r)
    def peri(self):
        super(Circle, self).peri();
        print(2*3.14*self.r)
class Triangle(Circle):
    def area(self):
        super(Triangle, self).area()
        print(0.5*self.b*self.h)
ob=Triangle()
ob.area()
ob.peri()
