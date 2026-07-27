# def display_name(*args):
#     for arg in args:
#         print(arg, end =" ")

# display_name("Mr." "Spongebob", "Squarepants" "III")

#args = allows you to pass multiple non-key arguments

def print_add(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}, {value}")
        # print(type(kwargs))

print_add(street="432 St. Lane, " \
        "RB road", 
        state="MH", 
        city="Mumbai", 
        zip=5432,)
#**kwargs = allows you to pass multiple keyword-arguments



def note(*args):
    for arg in args:
        print(arg, end=" ")
note("Hello", "Mr. Amarjeet", "Sahu")

