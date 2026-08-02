# Name: Navya
# Program: Logical Operators

percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))

eligible = percentage > 75 and attendance > 90

print("Eligible for scholarship:", eligible)

# Sample Output 1:
# Enter percentage: 82
# Enter attendance %: 95
# Eligible for scholarship: True

# Sample Output 2:
# Enter percentage: 70
# Enter attendance %: 92
# Eligible for scholarship: False