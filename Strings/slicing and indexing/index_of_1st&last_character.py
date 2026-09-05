s = input("Enter a string: ")
ch = input("Enter the character: ")
first = s.find(ch)
last = s.rfind(ch)
if first == -1:
    print("Character not found")
else:
    print("First occurrence index:", first)
    print("Last occurrence index:", last)
#Enter a string: navya
#Enter the character: a
#First occurrence index: 1
#Last occurrence index: 4
