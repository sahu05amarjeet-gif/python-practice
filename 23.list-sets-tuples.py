# Collection = single "Variable" used to store multiple values.
# List = [] ordered and changeable. Duplicates OK.
# Sets = {} unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuples = () ordered and unchangeable. Duplicates OK. Faster

cars = ["volvo", "benz", "maruti", "ferrari"]
# print(dir(cars))
# print(help(cars))
# print(len(cars))
# print("audi" in cars)


# cars[0] = "audi" -> Lists. Can change the variable after declaring.
# cars.append("audi")
# cars.remove("benz")
# cars.insert(0, "audi")
# cars.sort()
# cars.reverse()
# print(cars.index("benz"))
# print(cars)

# for car in cars:
#     print(car)

# Sets

fruits = {"orange", "banana", "coconut", "strawberry"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("cherry" in fruits)

# print(fruits[0]) -> We will get error as sets are unordered
# fruits.add("pineapple")
# fruits.remove("strawberry")
# fruits.pop()
# fruits.clear()

# print(fruits)


# Tuples

country = ("India", "Australia", "Japan", "Zimbabwe", "India")

# print(dir(country))
# print(help(country))
# print(len(country))
# print("New Zealand" in country)

print(country.index("Zimbabwe"))
print(country.count("India"))



