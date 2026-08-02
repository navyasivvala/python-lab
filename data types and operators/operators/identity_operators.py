# Name: Navya
# Program: Identity Operators

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))

# Sample Output:
# list1 == list2: True
# list1 is list2: False
# list1 is list3: True
# ID of list1: 2324567891232
# ID of list2: 2324567891584
# ID of list3: 2324567891232