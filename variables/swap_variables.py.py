#Navya

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

# (a) Using temporary variable
temp = a
a = b
b = temp

print("\nAfter Swapping using Temporary Variable:")
print("a =", a)
print("b =", b)

# Reset values
a = 10
b = 20

# (b) Using tuple unpacking
a, b = b, a

print("\nAfter Swapping using Tuple Unpacking:")
print("a =", a)
print("b =", b)