Student = {
    101: {"name": "Rahul", "dept": "CSE", "marks": 85},
    102: {"name": "Priya", "dept": "CSE", "marks": 92},
    103: {"name": "Amit", "dept": "ECE", "marks": 78},
    104: {"name": "Sneha", "dept": "CSE", "marks": 92},
    105: {"name": "Arjun", "dept": "IT", "marks": 88}
}

# 1. Sort the dictionary according to marks (highest to lowest)
sorted_students = dict(
    sorted(Student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("1. Students sorted by marks:")
for roll, details in sorted_students.items():
    print(roll, details)


# 2. Print record of students who scored maximum marks
max_marks = max(Student.values(), key=lambda x: x["marks"])["marks"]

print("\n2. Students with maximum marks:")
for roll, details in Student.items():
    if details["marks"] == max_marks:
        print(roll, details)


# 3. Find average marks
avg_marks = sum(
    map(lambda x: x["marks"], Student.values())
) / len(Student)

print("\n3. Average marks =", avg_marks)


# 4. Print students who scored more than average
print("\n4. Students scoring more than average:")
for roll, details in Student.items():
    if details["marks"] > avg_marks:
        print(roll, details)
