import re
# 1. Redact every email address
text = "Contact us at abc@gmail.com or support@example.com for more information."
hidden_text = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "[EMAIL HIDDEN]", text)
print("Email redacted:")
print(hidden_text)

# 2. Convert "Doe, John" to "John Doe" using groups and back-references
names = "Doe, John"

converted_name = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", names)

print("\nConverted name:")
print(converted_name)


# 3. Double every number using a replacement function
sentence = "I have 3 apples and 5 oranges."

def double_number(match):
    number = int(match.group())
    return str(number * 2)

doubled_sentence = re.sub(r"\d+", double_number, sentence)

print("\nDoubled numbers:")
print(doubled_sentence)


# 4. Collapse repeated punctuation using re.subn()
sample = "Wait!!! What??? Really!!"

collapsed, replacements = re.subn(r"([!?])\1+", r"\1", sample)

print("\nCollapsed punctuation:")
print(collapsed)
print("Number of replacements:", replacements)
