n = int(input("Enter a number: "))
original = n
reverse = 0
digit_sum = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    digit_sum += digit
    n //= 10

print("\n--- Number Analysis ---")
print("Original Number:", original)
print("Reversed Number:", reverse)
print("Sum of Digits:", digit_sum)

if original == reverse:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

if original > 1:
    prime = True

    for i in range(2, int(original ** 0.5) + 1):
        if original % i == 0:
            prime = False
            break

    if prime:
        print("Prime: Yes")
    else:
        print("Prime: No")
else:
    print("Prime: No")
