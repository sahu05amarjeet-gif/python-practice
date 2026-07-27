#Static method = Which depends on class but doesn't require any objects to call it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Cleaner", "Waiter"]
        return position in valid_positions
    
employee1 = Employee("Gengar", "Cook")
employee2 = Employee("Jai", "Manager")
employee3 = Employee("Ram", "Waiter")

    
print(Employee.is_valid_position("Sportsperson"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())