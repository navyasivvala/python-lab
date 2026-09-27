from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Anu", "department": "HR", "salary": 35000},
    {"name": "Rahul", "department": "IT", "salary": 50000},
    {"name": "Priya", "department": "Finance", "salary": 45000},
    {"name": "Kiran", "department": "IT", "salary": 30000}
]

department = "IT"

selected = list(filter(
    lambda emp: emp["department"] == department,
    employees
))

hiked = list(map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "salary": emp["salary"] * 1.10
    },
    selected
))

total_salary = reduce(
    lambda a, b: a + b["salary"],
    hiked,
    0
)

print("Selected employees:")
print(hiked)

print("Total salary expenditure after hike:", total_salary)
#Selected employees:
#[{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}, {'name': 'Rahul', 'department': 'IT', 'salary': 55000.00000000001}, {'name': 'Kiran', 'department': 'IT', 'salary': 33000.0}]
#Total salary expenditure after hike: 132000.0
