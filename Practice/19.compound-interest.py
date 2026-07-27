principle = 0
rate = 0
time = 0

while(principle<=0):
    principle = int(input("Enter the principle: "))
    if(principle<=0):
        print("Principle cannot be in negative")

while(rate<=0):
    rate = int(input("Enter the rate of the interest: "))
    if(rate<=0):
        print("rate cannot be in negative")

while(time<=0):
    time = int(input("Enter the time in years: "))
    if(time<=0):
        print("time cannot be in negative")

total = principle*pow((1+ rate/100),time)

print(f"Balance after {time} year/s: ${total:.2f}")