from functools import reduce

numbers = [2, 4, 6, 8]

product = reduce(lambda a, b: a * b, numbers)

maximum = reduce(lambda a, b: a if a > b else b, numbers)

words = ["Python", "is", "easy", "to", "learn"]

sentence = reduce(lambda a, b: a + " " + b, words)

print("Product:", product)
print("Maximum:", maximum)
print("Sentence:", sentence)
#Product: 384
#Maximum: 8
#Sentence: Python is easy to learn
