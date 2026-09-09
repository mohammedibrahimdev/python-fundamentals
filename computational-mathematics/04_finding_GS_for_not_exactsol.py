import sympy as sp

# ---------------------------------------------------------
# Problem:
# Find the General Solution of a first-order differential
# equation:
#
#     M(x,y) dx + N(x,y) dy = 0
#
# The program:
# 1. Takes M(x,y) and N(x,y) as input.
# 2. Checks whether the D.E. is exact.
# 3. If exact, directly finds the general solution.
# 4. If not exact, checks for Type-3 and Type-4
#    integrating factors.
# 5. Uses the integrating factor to make the D.E. exact.
# 6. Finds the general solution.
# ---------------------------------------------------------


# Create symbolic variables
x, y, c = sp.symbols('x y c')


# Take M(x,y) and N(x,y) as input
M = sp.sympify(input("Enter value of M(x,y): "))
N = sp.sympify(input("Enter value of N(x,y): "))


# Find partial derivatives:
# ∂M/∂y and ∂N/∂x
diff_of_M = sp.diff(M, y)
diff_of_N = sp.diff(N, x)

print(f"The diff of M(x,y): {diff_of_M}")
print(f"The diff of N(x,y): {diff_of_N}")


# ---------------------------------------------------------
# Check whether the differential equation is exact
#
# Exact condition:
#     ∂M/∂y = ∂N/∂x
# ---------------------------------------------------------

if diff_of_M == diff_of_N:

    print("The given D.E is Exact.")

    # Integrate M with respect to x
    F = sp.integrate(M, x)

    # Find the remaining part by integrating with respect to y
    G = sp.integrate(N - sp.diff(F, y), y)

    print("The General Solution:")
    sp.pprint(sp.Eq(F + G, c))


else:

    print("The given D.E is NOT Exact.")


    # Find possible Type-3 and Type-4 integrating factors

    type3 = sp.simplify((diff_of_M - diff_of_N) / N)
    type4 = sp.simplify((diff_of_N - diff_of_M) / M)

    Integration_Factor = None


    # Type-3 integrating factor
    if not type3.has(y):

        Integration_Factor = sp.exp(sp.integrate(type3, x))

        print("The Integrating Factor (Type-3):")
        sp.pprint(Integration_Factor)


    # Type-4 integrating factor
    elif not type4.has(x):

        Integration_Factor = sp.exp(sp.integrate(type4, y))

        print("The Integrating Factor (Type-4):")
        sp.pprint(Integration_Factor)


    else:

        print("Type-3 and Type-4 integrating factors are not applicable.")


    # Solve the D.E. after finding the integrating factor

    if Integration_Factor is not None:

        # Multiply both M and N by the integrating factor
        M1 = sp.simplify(M * Integration_Factor)
        N1 = sp.simplify(N * Integration_Factor)

        # Integrate the new M
        F = sp.integrate(M1, x)

        # Find the remaining part
        G = sp.integrate(N1 - sp.diff(F, y), y)

        print("The General Solution:")
        sp.pprint(sp.Eq(F + G, c))