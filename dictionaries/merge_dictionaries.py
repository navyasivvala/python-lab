dict1 = {
    1: "Apple",
    2: "Banana"
}

dict2 = {
    3: "Mango",
    4: "Orange"
}

# Using update()
merged1 = dict1.copy()
merged1.update(dict2)
print("Using update():", merged1)

# Using | operator
merged2 = dict1 | dict2
print("Using | operator:", merged2)
