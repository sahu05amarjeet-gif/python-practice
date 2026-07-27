# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
 
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5
    
# class Pizza(Circle):
#     def __init__(self, toppings, radius):
#         self.toppings = toppings
#         super().__init__(radius)

# shapes = [Circle(4), Square(2), Triangle(2, 4), Pizza("Pepperoni", 20)]

# for shape in shapes:
#     print(shape.area())

#Polymorphism for Inheritence -> An obj could be treated of the same type as parent class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        return "Move!"
        

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        return "Sail!!"
class Plane(Vehicle):
    def move(self):
        return "Fly!!"

vehicles = [Car("Range Rover", "XY7"), Boat("Ibiza", "Touring 20"), Plane("Boeing", "747")]

for vehicle in vehicles:
    print(vehicle.brand)
    print(vehicle.model)

    print(vehicle.move())

#In simpler terms = Polymorphism = same method for all the classes





