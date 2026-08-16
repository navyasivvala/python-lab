n = int(input("Enter a number: "))

temp = n
sum = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    count += 1
    temp //= 10

average = sum / count

print("Sum =", sum)
print("Average =", average)
#output
#Enter a number: 23
#Sum = 5
#Average = 2.5
