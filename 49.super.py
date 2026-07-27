#super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'} ")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"The area of the circle is {3.14 * self.radius * self.radius}cm^2") 
        #Method Overwriting (Prefers Child Method over Parents)
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"The area of square is {self.width * self.width} cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, heigth):
        super().__init__(color, is_filled)
        self.width = width
        self.heigth = heigth

    def describe(self):
        print(f"The area of Triangle is {self.width * self.heigth / 2} cm^2")
        super().describe()

shape = Shape("Red", True)
circle = Circle(color="Red", is_filled=True,  radius=20)
square = Square(color="Yellow", is_filled=True, width=4)
triangle = Triangle(color="Brown", is_filled=False, width=2, heigth=2)

circle.describe()
square.describe()
triangle.describe() 

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.heigth)
