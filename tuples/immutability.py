numbers = (10, 20, 30)

try:
    numbers[1] = 50
except TypeError as e:
    print("Error:", e)
