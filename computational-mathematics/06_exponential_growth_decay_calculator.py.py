import math

# Get initial values
n = float(input("Enter the initial amount: "))
N0 = float(input("Enter the next amount: "))
t0 = float(input("Enter the next time: "))

# Calculate constants
C = n
K = math.log(N0 / n) / t0

print(f"Constant C = {C}")
print(f"Growth/Decay constant K = {K:.6f}")

# Display menu
print("\n1. Calculate amount when time is given")
print("2. Calculate time when amount is given")

choice = int(input("Enter your choice: "))

if choice == 1:
    t1 = float(input("Enter the time: "))
    N1 = C * math.exp(K * t1)
    print(f"Amount of substance = {N1:.4f}")

elif choice == 2:
    N1 = float(input("Enter the amount: "))

    if K == 0:
        if N1 == n:
            print("The amount remains constant at all times.")
        else:
            print("The given amount cannot be reached.")
    else:
        t1 = math.log(N1 / n) / K
        print(f"Time = {t1:.4f}")

else:
    print("Invalid choice!")