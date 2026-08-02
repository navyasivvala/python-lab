# Task 1
# Name: Navya

import sys

if len(sys.argv) != 2:
    print("Usage: python greet.py <name>")
else:
    name = sys.argv[1]
    print("Hello,", name + "!")