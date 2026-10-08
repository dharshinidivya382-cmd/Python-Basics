import math

n = int(input("Enter a number: "))

original = n
total = 0

while n > 0:
    digit = n % 10
    total += math.factorial(digit)
    n //= 10

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
