#Python calculator

# print("--------------PYTHON CALCUALTOR--------------")
# while True:
#     first_num = float(input("Enter the first number: "))
#     operator = input("Enter the operator (+, -, /, *): ")
#     sec_num = float(input("Enter the second number: "))

#     if(operator == "+"):
#         print(first_num + sec_num)
#     elif(operator == "-"):
#         print(first_num - sec_num)
#     elif(operator == "*"):
#         print(first_num * sec_num)
#     elif(operator == "/"):
#         print(first_num / sec_num)
#     else:
#         print("Not a valid operator!")

#Checking Triangle 
while True:
    a = float(input("Enter the first side of triangle: "))
    b = float(input("Enter the second side of triangle: "))
    c = float(input("Enter the third side of triangle: "))

    if(a == b == c):
        print("Equilateral triangle")
    elif(a == b or b == c or a == c):
        print("Isosceles triangle")
    elif(a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b):
        print("Right angled triangle")
    else:
        print("ERROR 404")