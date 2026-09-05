s = input("Enter a string: ")
count = {}
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
print("Duplicate characters and their counts:")
for ch in count:
    if count[ch] > 1:
        print(ch, ":", count[ch])
#Enter a string: navya
#Duplicate characters and their counts:
#a : 2
