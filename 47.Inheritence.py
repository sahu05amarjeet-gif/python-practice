# Inheritence = Allows a class to inherit attributes and methods from another class
       #         Helps with code resuability and extensibility
       #         class Child(Parent)

class Animals:
    def __init__(self, name):
        self.name = name
        self.is_Alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animals):
    def speak(self):
        print("WOOOF")

class Cat(Animals):
    pass

class Mouse(Animals):
    pass

dog = Dog("Billu")

cat = Cat("Komal")

mouse = Mouse("Jerry")

# print(dog.is_Alive)
# print(cat.name)
# print(mouse.is_Alive)
mouse.eat()
cat.sleep()
print(dog.name)
dog.speak()

