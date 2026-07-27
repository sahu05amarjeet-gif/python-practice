class Students:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students are {cls.count}"
    @classmethod
    def get_gpa(cls):
        return f"{cls.total_gpa / cls.count:.2f}"
    
students1 = Students("Amar", 4.8)
students2 = Students("Rohan", 4.3)
students3 = Students("Chinmay", 3.2)

print(Students.get_count())
print(Students.get_gpa())

#Class Methods = Best for class-level data or require access to the class itself.
#Static Methods = Best for utility methods that doesn't require the access to class data
