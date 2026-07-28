def bmi(weight, height):
    calculate_bmi = weight/(height ** 2)
    if calculate_bmi <= 18.5:
        return "Underweight"
    elif calculate_bmi <= 25.0:
        return "Normal"
    elif calculate_bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

print(bmi(98, 173))