s = input("Enter a string: ")
sLen = len(s)
reversed_str = ""

for char in s:
        reversed_str = char + reversed_str

print(reversed_str)