# format specifier = {value.flags} format a value on what flags are 
#                       flags are inserted.

# price1 = 332.445
# price2 = 33.23
# price3 = 3.412

# print(f"Price 1 is {price1:.2f}")
# print(f"Price 2 is {price2:.2f}")
# print(f"Price 3 is {price3:.2f}")

# price1 = 332.445
# price2 = 33.23
# price3 = 3.412

# print(f"Price 1 is {price1:10}")
# print(f"Price 2 is {price2:10}")
# print(f"Price 3 is {price3:10}")

price1 = 332.445
price2 = 33.23
price3 = 3.412

print(f"Price 1 is {price1:010}") # similarly we can use "<" which left indent the value.
print(f"Price 2 is {price2:010}")
print(f"Price 3 is {price3:010}")

# >, +, ^ 