
groceries = [["Mangoes", "Bananas", "Oranges", "Pineapple"],
            ["Raddish", "Carrots", "Mushroom", "Peas"],
            ["Chicken", "Lamb", "Turkey", "Fish"]]

for collections in groceries:
    for food in collections:
        print(food, end=" ")
    print()