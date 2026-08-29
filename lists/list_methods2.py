numbers = [30, 10, 20, 10, 40]

print("Original List:", numbers)

numbers.append(50)
print("After append():", numbers)

numbers.insert(1, 15)
print("After insert():", numbers)

numbers.extend([60, 70])
print("After extend():", numbers)

numbers.remove(10)
print("After remove():", numbers)

numbers.pop()
print("After pop():", numbers)

numbers.sort()
print("After sort():", numbers)

numbers.reverse()
print("After reverse():", numbers)

print("Count of 10:", numbers.count(10))

print("Index of 40:", numbers.index(40))
