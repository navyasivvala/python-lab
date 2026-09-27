count = 0
def fibonacci(n):
    global count

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("First 15 Fibonacci terms:")

for i in range(15):
    print(fibonacci(i), end=" ")


# Counting how many times fibonacci(5) is called while calculating fibonacci(10)

count = 0


def fibonacci_count(n):
    global count

    if n == 5:
        count = count + 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_count(n - 1) + fibonacci_count(n - 2)


fibonacci_count(10)

print("\nNumber of times fibonacci(5) is computed:", count)
#First 15 Fibonacci terms:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
#Number of times fibonacci(5) is computed: 8
