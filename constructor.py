# Create a class Student with attributes Name, dept, roll no.
# Initialize the attribute with constructor.
# Display the record of student using show().
# Define 5 student object and show records of 5 students.

class Student:
    def __init__(self, name, dept, roll_no):
        self.name = name
        self.dept = dept
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Roll No:", self.roll_no)
        print("\n")

s1 = Student("Rahul", "CSE", 101)
s2 = Student("Amit", "CSE", 102)
s3 = Student("Priya", "AIML", 103)
s4 = Student("Ankit", "ECE", 104)
s5 = Student("Sneha", "CSE", 105)

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()