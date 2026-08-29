data = (10, 20, [30, 40, 50])

data[2][1] = 100

print("Modified tuple:", data)

# Tuple is immutable, but the list inside the tuple is mutable.
# Therefore, the contents of the nested list can be modified.
