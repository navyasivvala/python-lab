import re
paragraph = "NASA is working with the USA on advanced technology. Scientists developed powerful systems for research."
# 1. Find all words written in CAPITAL letters
capital_words = re.findall(r"\b[A-Z]+\b", paragraph)
print("Capital words:", capital_words)
# 2. Find every word longer than 6 characters using finditer()
print("Words longer than 6 characters:")
long_words = re.finditer(r"\b[A-Za-z]{7,}\b", paragraph)
for match in long_words:
    print(match.group(), "starts at index", match.start())
# 3. Extract all dollar amounts
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r"\$\d+\.\d+", prices)
print("Dollar amounts:", amounts)
# 4. Count how many times the pattern occurs
count = len(re.findall(r"\b[A-Z]+\b", paragraph))
print("Number of capital words:", count)
#Capital words: ['NASA', 'USA']


#output
#Words longer than 6 characters:
#working starts at index 8
#advanced starts at index 32
#technology starts at index 41
#Scientists starts at index 53
#developed starts at index 64
#3powerful starts at index 74
#systems starts at index 83
#research starts at index 95
#Dollar amounts: ['$3.50', '$1.20', '$4.75']
#Number of capital words: 2
