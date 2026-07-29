import matplotlib.pyplot as plt
import numpy as np

print("Enter only a 2x2 matrix:")
print("Enter the matrix values row-wise:")

matrix = []

for i in range(2):
    row = list(map(float , input().split()))
    matrix.append(row)

matrix = np.array(matrix)

eigen_values , eigen_vectors = np.linalg.eig(matrix)

print("Eigen values : ")
print(eigen_values)

print("Eigen vectors :")
print(eigen_vectors)

plt.figure()

plt.axhline(0, color = 'black')
plt.axvline(0, color = 'black')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.quiver(
    0, 0,
    eigen_vectors[0, 0], eigen_vectors[1, 0],
    angles = 'xy',
    scale_units = 'xy',
    scale = 1,
    color = 'red'
)

plt.quiver(
    0, 0,
    eigen_vectors[0,1], eigen_vectors[1 ,1],
    angles = 'xy', 
    scale_units = 'xy',
    scale = 1,
    color = 'blue'
)

plt.title("GRAPHICAL REPRESENTATION OF EIGEN VECTORS ")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()