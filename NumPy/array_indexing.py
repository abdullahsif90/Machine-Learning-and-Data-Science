import numpy as np

print("Advanced Array Indexing & Slicing")

# Create 5x5 array
arr = np.arange(1, 26).reshape(5, 5)

print("\nOriginal Array:")
print(arr)


# 1. First row
first_row = arr[0]

print("\n1. First Row:")
print(first_row)


# 2. Last row
last_row = arr[-1]

print("\n2. Last Row:")
print(last_row)


# 3. First column
first_column = arr[:, 0]

print("\n3. First Column:")
print(first_column)


# 4. Last column
last_column = arr[:, -1]

print("\n4. Last Column:")
print(last_column)


# 5. Middle element
middle_element = arr[2, 2]

print("\n5. Middle Element:")
print(middle_element)


# 6. Top-left 3x3
top_left = arr[:3, :3]

print("\n6. Top-left 3x3:")
print(top_left)


# 7. Bottom-right 2x2
bottom_right = arr[-2:, -2:]

print("\n7. Bottom-right 2x2:")
print(bottom_right)


# 8. Alternate rows
alternate_rows = arr[::2]

print("\n8. Alternate Rows:")
print(alternate_rows)


# 9. Alternate columns
alternate_columns = arr[:, ::2]

print("\n9. Alternate Columns:")
print(alternate_columns)


# 10. All even numbers
even_numbers = arr[arr % 2 == 0]

print("\n10. Even Numbers:")
print(even_numbers)