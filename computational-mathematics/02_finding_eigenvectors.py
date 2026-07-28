"""
Problem: Finding Eigenvectors of a Matrix

Description:
This program takes a square matrix as input from the user,
calculates its eigenvalues and corresponding eigenvectors,
and displays the results.
"""

import numpy as np

# Taking order of matrix
n = int(input("Enter matrix order: "))

matrix = []

# Taking matrix input row wise
print("Enter matrix values row wise:")

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert list into NumPy array
matrix = np.array(matrix)

# Find eigenvalues and eigenvectors
eigen_values, eigen_vector = np.linalg.eig(matrix)

# Display results
print("Eigen Values:")
print(eigen_values)

print("\nEigen Vectors:")
print(eigen_vector)