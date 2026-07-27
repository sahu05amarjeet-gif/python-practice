#   functions = A block of reusable code
#   place () after the function name to invoke it

# def happy_bd(name, age):
#     print(f"Happy birthday to {name} ji")
#     print(f"You are {age} years old!")

# happy_bd("Amar", 20)
# # happy_bd()
# # happy_bd()


def display_inv(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date} ")
display_inv("Sahil", 755.43, "04/03/2027")

# Return = statement used to end a function
#           and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("amar", "sahu")
print(full_name)