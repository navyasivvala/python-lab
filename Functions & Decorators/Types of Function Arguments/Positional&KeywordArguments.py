def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


print("Using Positional Arguments:")
student_info("Navya", 101, "CSE")

print("\nUsing Keyword Arguments:")
student_info(branch="CSE", name="Navya", roll_no=101)

#Using Positional Arguments:
#Name: Navya
#Roll No: 101
#Branch: CSE

#Using Keyword Arguments:
#Name: Navya
#Roll No: 101
#Branch: CSE
