s = input("Enter a string: ")
result = ""
for ch in s:
    if not ch.isspace():
        result += ch
print("String without whitespace:", result)
#Enter a string: navya sivvala
#String without whitespace: navyasivvala
