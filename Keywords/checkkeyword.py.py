#navya

import keyword
word=input("enter a word:")
if keyword.iskeyword(word):
 print(word,"is a python keyword.")
else:
 print(word,"is not a python keyword.")