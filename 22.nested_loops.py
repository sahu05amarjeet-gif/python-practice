# Nested Loops = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the number of rows: "))
coloums = int(input("Enter the number of coloums: "))
symbol = input("Enter the symbol: ")


for x in range(rows):
    for y in range(coloums):
        print(symbol, end="")
    print()