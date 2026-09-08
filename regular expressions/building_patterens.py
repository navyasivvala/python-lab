import re
# 1. Pattern for a valid Python variable name
pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
variables = ["_count2", "2fast", "total_sum"]
print("Valid Python variable names:")
for variable in variables:
    if re.fullmatch(pattern, variable):
        print(variable, "-> Valid")
    else:
        print(variable, "-> Invalid")
# 2. Using alternation to match cat, dog, or bird as whole words
sentence = "I have a cat and a dog. My friend has a bird."
pets = re.findall(r"\b(cat|dog|bird)\b", sentence)
print("\nPets found:", pets)
# 3. Matching hexadecimal color codes with 3 or 6 hex digits
colors = "#FFAA00 #000 #12ABCD #12345"
color_codes = re.findall(r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?\b", colors)
print("\nValid hexadecimal color codes:", color_codes)
# 4. Using named groups to parse a log line
log = "2024-06-01 08:15:32 ERROR Disk full"
pattern = (
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>\w+) "
    r"(?P<message>.*)"
)
m = re.search(pattern, log)
print("\nLog details:")
print("Date:", m.group("date"))
print("Time:", m.group("time"))
print("Level:", m.group("level"))
print("Message:", m.group("message"))
#output
#Valid Python variable names:
#_count2 -> Valid
#2fast -> Invalid
#total_sum -> Valid
#Pets found: ['cat', 'dog', 'bird']
#Valid hexadecimal color codes: ['#FFAA00', '#000', '#12ABCD']
#Log details:
#Date: 2024-06-01
#Time: 08:15:32
#Level: ERROR
#Message: Disk full
