def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
for i in range(5):
    n = int(input("Enter a number: "))

    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd")

#output
#Enter a number: 5
#5 is Odd
#Enter a number: 3
#3 is Odd
#Enter a number: 2
#2 is Even
#Enter a number: 1
#1 is Odd
#Enter a number: 6
#6 is Even
