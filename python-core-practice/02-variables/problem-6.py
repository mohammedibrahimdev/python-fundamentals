"""
Problem 6: Student Information Card

Take the student's details as input:
- Name
- Roll Number
- Department
- Section
- CGPA
- Year

Print the student's information in the form of an ID card.
"""

student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number : ")
department = input("Enter Department : ")
section = input("Enter Section : ")
cgpa = float(input("Enter CGPA : "))
year = int(input("Enter Year : "))

print("\n======== STUDENT ========")
print(f"Name        : {student_name}")
print(f"Roll Number : {roll_number}")
print(f"Department  : {department}")
print(f"Section     : {section}")
print(f"CGPA        : {cgpa}")
print(f"Year        : {year}")
print("=========================")