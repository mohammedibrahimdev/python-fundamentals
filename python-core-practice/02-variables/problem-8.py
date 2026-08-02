"""
Problem 8: Simple Interest Calculator

Take the following as input:
- Principal Amount
- Rate of Interest
- Time (in years)

Calculate the Simple Interest using the formula:

Simple Interest = (Principal × Rate × Time) / 100

Print the Principal Amount, Rate, Time, and Simple Interest neatly.
"""

P = int(input("Enter original amount of money : "))
R = float(input("Enter Interest rate per year (in %) : "))
T = int(input("Enter Time : "))

print()
SI = (P * R *T)/100

print(f'Principle : {P}')
print(f'Rate      : {R}')
print(f'Time      : {T}')
print()
print(f"Simple Interest = {SI}")