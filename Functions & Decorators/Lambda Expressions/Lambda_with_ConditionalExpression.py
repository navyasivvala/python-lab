# Task 2: Lambda with Conditional Expression

grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = [35, 45, 67, 28, 80, 39]

for m in marks:
    print(m, grade(m))
#35 Fail
#45 Pass
#67 Pass
#28 Fail
#80 Pass
#39 Fail
