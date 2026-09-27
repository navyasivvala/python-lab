def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


total, average = total_marks(80, 90, 85)
print("3 Marks - Total:", total, "Average:", average)

total, average = total_marks(75, 80, 85, 90, 95)
print("5 Marks - Total:", total, "Average:", average)

total, average = total_marks(88)
print("1 Mark - Total:", total, "Average:", average)
#3 Marks - Total: 255 Average: 85.0
#5 Marks - Total: 425 Average: 85.0
#1 Mark - Total: 88 Average: 88.0

