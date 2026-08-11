print("Matrix Analyzer")

import numpy as np

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):

    row = []

    for j in range(columns):
        value = int(input(f"Enter value for row {i + 1}, column {j + 1}: "))
        row.append(value)

    matrix.append(row)

matrix = np.array(matrix)

print("\nMatrix:")
print(matrix)

print("\n**** Matrix Information ****")

print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Number of dimensions:", matrix.ndim)

print("Total sum:", np.sum(matrix))

print("cow-wise sum:", np.sum(matrix, axis=1))

print("column-wise sum:", np.sum(matrix, axis=0))

print("Maximum value:", np.max(matrix))
print("Minimum value:", np.min(matrix))