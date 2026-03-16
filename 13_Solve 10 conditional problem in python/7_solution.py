order_size = "Medium"
extra_shot = input("Enter yes or no for extra shot: ").lower()

extra_shot = extra_shot == "yes"

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)