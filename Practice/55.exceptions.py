try: 
    number = int(input("Enter the number: "))
    print(1 / number)

except ZeroDivisionError:
    print("You can't divide it by zero!")

except ValueError:
    print("You can't divide it by any string")

except Exception:
    print("Something went wrong!")

finally:
    print("Done!")