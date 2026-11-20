import numpy as np

# Create a 2D matrix
matrix = [[1, 2],
          [3, 4]]

# Convert into NumPy array
arr = np.array(matrix)

# Find transpose of the matrix
transpose = arr.T

# Print both matrices
print("Original Matrix:")
print(arr)

print("Transpose Matrix:")
print(transpose)
