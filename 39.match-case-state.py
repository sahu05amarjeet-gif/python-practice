# def days_of_week(day):
#     if day == 1:
#         print("Monday")
#     elif day == 2:
#         print("Tuesday") #And so on
    
#Match-case statement (switch): An alternative of using many 'elif' statements
# Execute some code if value matches a 'case'
# Benefit: Cleaner and syntax is more readable

# def days_of_week(day):
#     match day:
#         case 1:
#             return "It's Monday"
#         case 2:
#             return "It's Tuesday"
#         case 3: 
#             return "It's Wednesday"
#         case 4:
#             return "It's Thursday"
#         case _:
#             return "Not a valid date"
        
# print(days_of_week(5))


# def is_Weekend(days):
    # match days:
    #     case "Saturday" | "Sunday":
    #         return True
    #     case "Monday" | "Tuesday" | "Wednesday" "Thursday" | "Friday":
    #         return False
    #     case _:  #Wild card cases
    #         return False

# print(is_Weekend("Monday"))

def animals(scary):
    match scary:
        case "Lion" | "Tiger" | "Bear" | "Elephant":
            return True
        case "Dog" | "Cats" | "Sheep" | "Cow":
            return False
        case _ :
            return f"{scary} is an invalid input"
check = animals("Dog")
print(check)