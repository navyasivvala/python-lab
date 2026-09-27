# Task 3: Sorting with Lambda as key

students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]

result = sorted(students, key=lambda s: s[1], reverse=True)
print(result)

names = ["Ravi", "Sita", "Amit", "Raj"]

result = sorted(names, key=lambda x: len(x))
print(result)
#[('Sita', 92), ('Ravi', 78), ('Amit', 65)]
#['Raj', 'Ravi', 'Sita', 'Amit']
