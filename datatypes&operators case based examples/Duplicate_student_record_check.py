student1 = {"name": "Navya", "roll_no": 101}
student2 = student1
student3 = {"name": "Navya", "roll_no": 101}

print("student1 is student2:", student1 is student2)
print("student1 == student2:", student1 == student2)

print("student1 is student3:", student1 is student3)
print("student1 == student3:", student1 == student3)
#output
#student1 is student2: True
#student1 == student2: True
#student1 is student3: False
#student1 == student3: True
