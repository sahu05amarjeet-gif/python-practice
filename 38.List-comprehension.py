# num = []
# for x in range(1, 11):
#     num.append(x * 2)
# print(num)  # Traditional way of creating a list

#List Comprehension = A concise way to create a list in python
   #                   Compact and easier to read than traditional loops
 #                     [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]

# print(doubles)

# fruits = ["apple,", "banana", "guava", "watermelon"]

# fruits = [fruit[0] for fruit in fruits]

# print(fruits)


# nums = [1, -2, 3, -4, 5, -6, 8, -9, 10]

# pos_num = [num for num in nums if num >= 0]
# neg_num = [num for num in nums if num < 0]
# even_num = [num for num in nums if num % 2 == 0]
# odd_num = [num for num in nums if num % 2 == 1]


# print(pos_num)
# print(neg_num)
# print(even_num)
# print(odd_num)

# grades = [43, 54, 80, 90, 98, 65, 78]

# passing = [grade for grade in grades if grade >= 50]

# print(passing)


animals = ["Dog", "Sheep", "Cat", "Mouse"]
is_Alive = True
an = [animal[1] for animal in animals if is_Alive == True]

print(an)