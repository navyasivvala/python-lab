import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start, "seconds")

        return result
    return wrapper


@timer
def calculate_sum():
    total = 0

    for i in range(1, 1000001):
        total += i

    return total


result = calculate_sum()

print("Sum:", result)
#Execution time: 0.04355478286743164 seconds
#Sum: 500000500000
