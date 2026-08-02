#Navya

# Taking three subject marks in one line
marks = input("Enter 3 subject marks: ")

# Splitting and converting marks into integers
m1, m2, m3 = map(int, marks.split())

# Calculating average
average = (m1 + m2 + m3) / 3

# Printing average with 2 decimal places
print("Average: {:.2f}".format(average))