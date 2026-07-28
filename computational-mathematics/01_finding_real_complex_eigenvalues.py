"""
Problem: Finding Real and Complex Eigenvalues of a Matrix

Description:
This program takes a square matrix as input from the user,
calculates its eigenvalues, and checks whether each eigenvalue
is real or complex.
"""

import numpy as np


# Taking order of the matrix
n = int(input("Enter Order of the matrix: "))


# Creating an empty list to store matrix elements
matrix = []


# Taking matrix values row-wise from the user
print("Enter the matrix values row wise:")

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)


# Converting Python list into NumPy array
# NumPy array allows mathematical operations on matrices
matrix = np.array(matrix)


# Finding eigenvalues of the given matrix
eigen_values = np.linalg.eigvals(matrix)


# Displaying the calculated eigenvalues
print("Eigen values:")
print(eigen_values)
print()


# Checking whether eigenvalues are real or complex
for value in eigen_values:
    if np.iscomplex(value):
        print(value, "is a Complex Eigenvalue")
    else:
        print(value, "is a Real Eigenvalue")