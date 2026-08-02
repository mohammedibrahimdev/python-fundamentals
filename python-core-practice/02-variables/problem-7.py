"""
Problem 7: Salary Calculator

Take the following as input:
- Basic Salary
- HRA (House Rent Allowance)
- Bonus

Calculate the Gross Salary using the formula:

Gross Salary = Basic Salary + HRA + Bonus

Print the Basic Salary, HRA, Bonus, and Gross Salary neatly.
"""

Bs = int(input("Enter Basic Salary : "))
hra = int(input("Enter House Rent Allowance : "))
bsn = int(input("Enter Bonus : "))

print(F"Basic Salary   : {Bs}")
print(F"HRA            : {hra}")
print(F"Bonus          : {bsn}")

print(F"\nGross Salary : {Bs + hra + bsn}")