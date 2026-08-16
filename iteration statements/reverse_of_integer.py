n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number =", reverse)
#output
#Enter a number: 324
#Reversed number = 423
