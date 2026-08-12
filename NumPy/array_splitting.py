import numpy as np
arr = np.arange(1,25)
print("Numbers: ",arr)

# reshapping to 4*6
reshapped = arr.reshape(4,6)
print("Number converted after 4*6:")
print(reshapped)

# Transpose 
transpose_arr = np.transpose(reshapped)
print("\nTranspose of matrix: ")
print(transpose_arr)

# splitting into equal parts
splitting_arr = np.split(reshapped, 2,axis = 0)
print("Split matrix:")
print(splitting_arr)

# splitting the rows 
row_splitting = np.vsplit(reshapped,2)
print("Row splitting:")
print(row_splitting)

# column splitting
col_split = np.hsplit(reshapped , 2)
print("Column splitting:")
print(col_split)

# flatten 
flatten_arr = reshapped.flatten()
print("After flatten:")
print(flatten_arr)

# ravel
ravel_arr = np.ravel(reshapped)
print("After ravel:")
print(ravel_arr)