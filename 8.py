# Create a tuple of 20 employee names (with duplicates)
employees = (
    "Alice", "Bob", "Charlie", "David", "Alice",
    "Eva", "Frank", "George", "Bob", "Helen",
    "Ian", "Jack", "Kate", "Laura", "Mike",
    "Nina", "Oscar", "Alice", "Bob", "Peter"
)

print("Employee Tuple:")
print(employees)

# 1. Print each name and its frequency
print("\n1. Employee Name and Frequency:")
for name in set(employees):
    print(name, ":", employees.count(name))

# 2. Remove duplicate items and find distinct names
distinct_names = tuple(set(employees))
print("\n2. Distinct Employee Names:")
print(distinct_names)

# 3. Print the employee having maximum frequency
max_name = max(set(employees), key=employees.count)
print("\n3. Employee with Maximum Frequency:")
print(max_name, ":", employees.count(max_name), "times")

# 4. Sort the tuple in alphabetical order
sorted_names = tuple(sorted(employees))
print("\n4. Employees Sorted Alphabetically:")
print(sorted_names)

# 5. Input a specific employee name and check if it exists
search = input("\nEnter employee name to search: ")

if search in employees:
    print(search, "exists in the tuple.")
else:
    print(search, "does not exist in the tuple.")