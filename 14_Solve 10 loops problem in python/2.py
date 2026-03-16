# n = int(input("Enter a number: "))

# even_sum = 0

# for x in range(n):
#     if not(x % 2):
#         even_sum += x

# print(even_sum)

n = int(input("Enter a number: "))

even_sum = 0

for x in range(2, n+1, 2): # i = 0; i <= n; i+=2
        even_sum += x

print(even_sum)