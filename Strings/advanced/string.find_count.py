s = input("Enter the string: ")
sub = input("Enter the substring: ")

# Own find()
position = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        position = i
        break

# Own count()
count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1

print("First occurrence index:", position)
print("Number of occurrences:", count)
#Enter the string: helloworld
#Enter the substring: world
#First occurrence index: 5
#Number of occurrences: 1
