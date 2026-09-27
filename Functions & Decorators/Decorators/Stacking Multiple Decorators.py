import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@log_call
@timer
def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


result = calculate_sum(1000000)

print("Result:", result)
#Calling calculate_sum args=(1000000,) kwargs={}
#Execution time: 0.04144454002380371 seconds
#calculate_sum returned 500000500000
#Result: 500000500000


