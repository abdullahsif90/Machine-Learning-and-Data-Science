import numpy as np

print("Matrix Operations")

matrix_A = np.array([
    [5, 3, 9],
    [4, 12, 7],
    [6, 5, 8]
])

matrix_B = np.array([
    [8, 3, 7],
    [6, 5, 1],
    [11, 31, 23]
])

addition = matrix_A + matrix_B
subtraction = matrix_A - matrix_B
element_multiplication = matrix_A * matrix_B # for element
division = matrix_A / matrix_B

# actual multiplication like row and column 
matrix_multiplication = matrix_A @ matrix_B


flatten_A = matrix_A.flatten()
ravel_A = matrix_A.ravel()

flatten_B = matrix_B.flatten()
ravel_B = matrix_B.ravel()

print("\nMatrix A:")
print(matrix_A)

print("\nMatrix B:")
print(matrix_B)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)

print("\nElement-wise Multiplication:")
print(element_multiplication)

print("\nDivision:")
print(division)

print("\nMatrix Multiplication:")
print(matrix_multiplication)

print("\nFlatten A:")
print(flatten_A)

print("\nRavel A:")
print(ravel_A)

print("\nFlatten B:")
print(flatten_B)

print("\nRavel B:")
print(ravel_B)