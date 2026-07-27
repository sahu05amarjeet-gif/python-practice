#object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex: Phone, Cup, Book
#
#Class = (blueprint) used to design the structure and layout of an object
from pc import PC

pc1 = PC("Lenovo Ideapad slim 3", 2026, "Red Fox", False)
pc2 = PC("LOQ Ryzen 7", 2025, "Silver", True)
# print(pc1.laptop)
# print(pc1.year)
# print(pc1.color)
# print(pc1.is_forSale)

pc1.drive()
pc1.no_use()
pc2.describe()

