s = input("Enter a string: ")

if s.isdigit():
    print("The string contains only digits")
elif s.isalpha():
    print("The string contains only alphabets")
elif s.isalnum():
    print("The string is alphanumeric")
else:
    print("The string contains special characters")
#Enter a string: navya@0405
#The string contains special characters

