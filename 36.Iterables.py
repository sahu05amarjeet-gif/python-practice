# numbers = [1, 2, 3, 4, 5]
# for number in reversed(numbers):
#     print(number, end=" ")
#same with tuples, but sets are not reversible

my_dict = {"A": 1, "B": 2, "C": 3}
for key, value in my_dict.items():
    print(f"{key}:{value}")

#Iterables = An object/collection that returns its elements one at a time, allowing it
#           to be iterated over in a loop.


numbers = (1, 2, 3, 4, 5)
for number in reversed(numbers):
    print(number, end=" ")