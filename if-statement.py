import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

print(today)
print(dayofweek)

if dayofweek == 1:
    print("It's Tuesday.")

elif dayofweek == 0:
    print("It's not Tuesday.")
    print("It will be Tuesdy tommorow. ")
else:
    print("unfortunately, it's not Tuesday")

print("Thanks for checking if it's Tuesday.")