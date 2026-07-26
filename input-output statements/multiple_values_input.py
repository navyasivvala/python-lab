#Navya

# Taking multiple inputs in one line
numbers = input("Enter numbers separated by spaces: ")

# Splitting and converting into integers
values = numbers.split()
a = int(values[0])
b = int(values[1])
c = int(values[2])

# Printing sum
print("Sum:", a + b + c)