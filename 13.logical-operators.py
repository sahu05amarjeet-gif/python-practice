# logical operators = evaluate multiple conditions (or, and, not)
                    # or = atleast one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# temp = 25
# is_Raining = False


# if(temp > 30 or temp < 0 or is_Raining):
#     print("Party is cancelled")
# else: 
#     print("Party is scheduled")


temp = 30
is_sunny = True

if(temp>= 28 and is_sunny):
    print("It is cold outside")
elif(temp<=0 and is_sunny):
    print("It is sunny outside")
