capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "Japan": "Tokyo",
            "Russia": "Moscow"}

# print(capitals.get(""))

# if(capitals.get("China")):
#     print("That country does exists.")
# else:
#     print("That country's capital doesn't exists")

# capitals.update({"Kenya": "Nirobi"})
# capitals.update({"India": "Mumbai"})
# capitals.pop("Japan")
# capitals.popitem()
# # capitals.clear()

# print(capitals)


keys = capitals.keys()
# print(keys)           --> This returns an object which acts as a sets. We have to iterate over it. That's why we use for loop.


# for key in capitals.keys():
#     print(key)

values = capitals.values()

# for value in capitals.values():
#     print(value)

items = capitals.items()

for keys, values in capitals.items():
    print(f"{keys}: {values}")
