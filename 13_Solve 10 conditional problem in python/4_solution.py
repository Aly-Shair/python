
color = input("Enter color: ").lower()

status = "unripe" if color == "green" else "ripe" if color == "yellow" else "overripe" if color == "brown" else "inavlid color"

print(status)