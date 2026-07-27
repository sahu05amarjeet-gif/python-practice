#Duck Typing 
class Duck:
    def speak(self):
        print("Quack")

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

animals = [Duck(), Dog(), Cat()]
for animal in animals:
    animal.speak()

