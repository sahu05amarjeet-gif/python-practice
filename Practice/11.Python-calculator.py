# first_number = float(input("Enter the first Number: "))
# operator = input("Enter an operator (+ - * /): ")
# second_number = float(input("Enter the second Number: "))

# if (operator == "+"):
#     print(first_number + second_number)
# elif (operator == "-"):
#     print(first_number - second_number)
# elif (operator == "*"):
#     print(first_number * second_number)
# elif (operator == "/"):
#     print(round(first_number/second_number, 2))

# else: 
#     print(f"{operator} is not a valid operator")

# Python weight convertor

# weight = float(input("Enter your weight: "))
# units = input("Kilograms or Pounds? (K or L)")
# final_weight = weight * 2.205
# final_pound_weight = weight/2.205
# if(units == "K"):
#     # weight = weight * 2.205
#     units = "Lbs"
#     print(f"Your weight is {round(final_weight,2)} {units} ")
# elif(units == "L"):
#     # weight = weight / 2.205
#     units = "Kgs"
#     print(f"Your weight is {round(final_pound_weight,2)} {units}")

# else: 
#     print(f"{units} is not a valid unit.")


# Temp converter 

temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in celcius or Fahrenheit? (C/F): ")

if(unit == "C"):
    temp = round((9 * temp)/5 + 32, 2)
    unit = "Fahrenheit"
    print(f"The temperature is {temp} {unit}")
elif(unit == "F"):
    temp = round((temp - 32) * 5 / 9, 2)
    unit = "Celcius"
    print(f"The temperature is {temp} {unit}")
else:
    print(f"{unit} is not a valid unit")