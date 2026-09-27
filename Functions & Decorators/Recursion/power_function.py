def power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1 / power(base, -exp)


print("2 raised to 5:", power(2, 5))
print("2 raised to 0:", power(2, 0))
print("2 raised to -2:", power(2, -2))
#2 raised to 5: 32
#2 raised to 0: 1
#2 raised to -2: 0.25

