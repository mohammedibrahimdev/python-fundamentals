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