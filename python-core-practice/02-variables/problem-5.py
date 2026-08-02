"""
Problem 5: Student Marks Calculator

Take the student's name and marks for five subjects as input.
Calculate the total marks and average marks.
Print the student's details, subject marks, total, and average neatly.
"""

student_name = input("Enter Student Name : ")

math_marks = int(input("Enter Maths Marks : "))
physics_marks = int(input("Enter Physics Marks : "))
chemistry_marks = int(input("Enter Chemistry Marks : "))
english_marks = int(input("Enter English Marks : "))
python_marks = int(input("Enter Python Marks : "))

print(f"\nStudent Name   : {student_name}")
print(f"Maths          : {math_marks}")
print(f"Physics        : {physics_marks}")
print(f"Chemistry      : {chemistry_marks}")
print(f"English        : {english_marks}")
print(f"Python         : {python_marks}")

total_marks = (
    math_marks
    + physics_marks
    + chemistry_marks
    + english_marks
    + python_marks
)

average_marks = total_marks / 5

print(f"\nTotal Marks    : {total_marks}")
print(f"Average Marks  : {average_marks}")