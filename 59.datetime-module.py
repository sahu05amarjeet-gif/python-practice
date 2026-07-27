import datetime

today = datetime.date.today()
x = datetime.datetime.now()

print(today)
print(x.strftime("%H:%M:%S %d-%m-%Y"))

target_date = datetime.datetime(2032, 5, 12, 5, 0, 5)
current_date = datetime.datetime.now()

if target_date < current_date:
    print("Target date has been passed")

else:
    print("Target date has not passed")