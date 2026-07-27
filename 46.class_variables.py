#class variables = Shared among all the instances of a class
#                  Defined outside the constructor
#                  Allow you to share the data among all the objects created from that class
#                          

class Students: # <--- Class variable
    class_year = 2025
    num_of_students = 0 # <--- Used when we need to start a count.

    def __init__(self, name, age):
        self.name = name # <-- Instance of the class
        self.age = age
        Students.num_of_students += 1
    
student1 = Students("Arohi", 19) # <-- Objects
student2 = Students("Rohan", 22)

print(student1.name)
print(student1.age)
print(Students.class_year)

print(student2.name)
print(student2.age)
print(Students.class_year)

print(Students.num_of_students)

print(f"My graduating class of {Students.class_year} has {Students.num_of_students} students")