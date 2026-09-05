sentence = input("Enter a sentence: ")

words = sentence.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:])

print("Title Case:", " ".join(result))
#Enter a sentence: python is very tough
#Title Case: Python Is Very Tough

