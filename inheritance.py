class Shape:
    def area(self):
        print("Area method of Shape class")



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius



class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth



class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(8, 3)


print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())
print("Area of Triangle:", t.area())