items = {
    "Pen": 10,
    "Book": 50,
    "Bag": 800,
    "Pencil": 5
}

highest = max(items, key=items.get)
lowest = min(items, key=items.get)

print("Highest price item:", highest, items[highest])
print("Lowest price item:", lowest, items[lowest])
