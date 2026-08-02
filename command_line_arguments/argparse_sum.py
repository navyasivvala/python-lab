# Challenge Task
# Name: Navya

import argparse

parser = argparse.ArgumentParser(description="Add two numbers")

parser.add_argument("--num1", type=int, required=True, help="First number")
parser.add_argument("--num2", type=int, required=True, help="Second number")

args = parser.parse_args()

print("Sum:", args.num1 + args.num2)