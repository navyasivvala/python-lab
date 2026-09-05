s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)
#Enter a string: navya
#String after removing duplicates: navy

