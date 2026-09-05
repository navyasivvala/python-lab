s = input("Enter a string: ")
reverse = ""
for ch in s:
    reverse = ch + reverse
print("Reversed string without slicing:", reverse)
#with slicing
reverse = s[::-1]
print("Reversed string with slicing:", reverse)
#Enter a string: navya
#Reversed string without slicing: ayvan
#Reversed string with slicing: ayvan

