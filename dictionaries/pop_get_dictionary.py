student = {
    101: "Anu",
    102: "Bhavya",
    103: "Charan"
}

removed = student.pop(102)
print("Removed:", removed)
print("Dictionary:", student)

name = student.get(105, "Key does not exist")
print(name)
