import re
sentence = "1024 requests were served in 3 seconds"
# 1. Using re.match() 
m1 = re.match(r"\d", sentence)
if m1:
    print("Sentence starts with a digit:", m1.group())
else:
    print("Sentence does not start with a digit")
# 2. Using re.search() 
m2 = re.search(r"served", sentence)
if m2:
    print("The word 'served' is found at:", m2.span())
else:
    print("The word 'served' is not found")
# 3. Using re.fullmatch() 
m3 = re.fullmatch(r"\d+", "12345")

if m3:
    print("12345 contains only digits")
else:
    print("12345 does not contain only digits")
# Testing with "123a5"
m4 = re.fullmatch(r"\d+", "123a5")
if m4:
    print("123a5 contains only digits")
else:
    print("123a5 does not contain only digits")

#output
#Sentence starts with a digit: 1
#The word 'served' is found at: (19, 25)
#12345 contains only digits
#123a5 does not contain only digits
