start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))

print("Prime numbers are:")

for n in range(start, end + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
#output
#Enter lower limit: 10
#Enter upper limit: 30
#Prime numbers are:
#11 13 17 19 23 29 
        
