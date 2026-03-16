n = int(input("Enter a number greater than 1: "))

isPrime = True

for i in range(2, n):
    if n%i == 0:
        isPrime = False
        break
if(n < 2):
    print("not prime")
elif(isPrime):
    print("prime")
else:
    print("not prime")