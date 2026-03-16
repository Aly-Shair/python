from datetime import datetime

day = datetime.today().weekday()

age = int(input("Enter your age: "))

price = 8 if age < 18 else 12 # tertiary operator

if day == 2:
    price -= 2

print(f"Your price is: {price}$")