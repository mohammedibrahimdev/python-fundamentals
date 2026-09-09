import sympy as sp

# ---------------------------------------------------------
# Problem:
# Solve Newton's Law of Cooling.
#
# Formula:
#     T(t) = Ts + (T0 - Ts)e^(-kt)
#
# Where:
#     T  = temperature of the object at time t
#     Ts = surrounding (ambient) temperature
#     T0 = initial temperature of the object
#     T1 = temperature of the object at time t1
#     k  = cooling constant
#
# The program:
# 1. Takes the surrounding, initial and known temperature values.
# 2. Finds the constant C.
# 3. Uses the second temperature condition to find k.
# 4. Builds the final temperature equation.
# 5. Finds the temperature at a required time.
# ---------------------------------------------------------


# Create symbolic variables
t, k, C = sp.symbols('t k C')


# Take input values from the user
Ts = sp.sympify(input("Enter surrounding temperature: "))
T0 = sp.sympify(input("Enter initial temperature: "))
T1 = sp.sympify(input("Enter temperature after t1: "))
t1 = sp.sympify(input("Enter t1: "))


# General form of Newton's Law of Cooling
# T(t) = Ts + C * e^(-kt)
T = Ts + C * sp.exp(-k * t)

print("\nNewton's Law of Cooling:")
sp.pprint(T)



# Find C using the initial condition:
# T(0) = T0

# Substitute t = 0 into the temperature equation
equation_C = sp.Eq(T.subs(t, 0), T0)

# Solve the equation for C
C_value = sp.solve(equation_C, C)[0]

print("\nValue of C:")
sp.pprint(C_value)


# Replace C with its calculated value
T = T.subs(C, C_value)


# Find k using the second condition:
# T(t1) = T1

# Substitute t = t1 into the temperature equation
equation_k = sp.Eq(T.subs(t, t1), T1)

# Solve the equation for k
k_value = sp.solve(equation_k, k)[0]

print("\nValue of k:")
sp.pprint(k_value)


# Replace k with its calculated value
T = T.subs(k, k_value)



# Final temperature equation

print("\nFinal Temperature Equation:")
sp.pprint(T)


# Find temperature at any required time

# Take the required time from the user
t_required = sp.sympify(input("\nEnter required time: "))

# Substitute the required time into T(t)
T_required = T.subs(t, t_required)

print("\nTemperature at required time:")
sp.pprint(T_required)