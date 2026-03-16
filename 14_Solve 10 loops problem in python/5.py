input_str = input("Enter :")

ans = -1

for char in input_str:
    if input_str.count(char) == 1:
        ans = char
        break
print(ans)