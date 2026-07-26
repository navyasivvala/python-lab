# Task 2
# Name: Navya

import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print("Sum:", num1 + num2)