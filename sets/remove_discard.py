my_set = {10, 20, 30, 40}

my_set.remove(20)
print("After remove:", my_set)

my_set.discard(30)
print("After discard:", my_set)

# Difference:
# remove() gives an error if the element does not exist.
# discard() does not give an error if the element does not exist.
