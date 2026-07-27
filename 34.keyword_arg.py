def greet(greetings, title, first_name, last_name):
    print(f"{greetings} {title}{first_name} {last_name}")

greet(greetings="Hello",first_name="Shekhar", last_name="Kakkar",title="Mr.")

#Keyword argument = an argument preceded by an identifier
# Helps with readability 
# Order of argument doesnt matter

# for x in range(0, 11):
#     print(x, end = " ")

# print("1", "2", "3", "4", sep = "-")

def phone(cc, areac, first, last):
    return f"{cc}-{areac}-{first}-{last}"
phone_num = phone(cc= 91, areac= 1234, first= 567, last= 890)

print(phone_num)


def DOB(user, date, month):
    print(f"Hey {user} your birthday is on {date}th of {month}")
DOB("Amar", 5,  "December")