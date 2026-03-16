
score = int(input("Enter your grade: "))

if score < 0 or score > 100:
    print("Please verify your grade again")
    exit()
    # return

if score < 60:
    print("F")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
elif score < 101:
    print("A")