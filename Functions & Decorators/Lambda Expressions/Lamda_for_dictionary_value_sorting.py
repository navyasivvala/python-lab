# Task 5: Lambda for Dictionary Value Sorting

items = {
    "Pen": 10,
    "Book": 50,
    "Pencil": 5,
    "Bag": 500
}

result = sorted(items.items(), key=lambda x: x[1])

print(result)

#[('Pencil', 5), ('Pen', 10), ('Book', 50), ('Bag', 500)]

