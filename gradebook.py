# Simple Student Grade Book
# Author: Mohamed Sallam

# Ask for the number of students
num_students = int(input("Enter the number of students: "))

# Dictionary to store student names and grades
students = {}

# Loop to collect student info
for i in range(1, num_students + 1):
    name = input(f"Enter name for student {i}: ")
    grade = input(f"Enter grade for {name}: ")
    students[name] = grade

# Lookup a student's grade
lookup_name = input("Enter student name to lookup: ")

if lookup_name in students:
    print(f"{lookup_name}'s grade is: {students[lookup_name]}")
else:
    print("Student not found.")
