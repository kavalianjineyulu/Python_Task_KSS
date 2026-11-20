import numpy as np

# Dataset
data = [5, 10, 15, 20, 25, 30]

# Convert list into NumPy array
arr = np.array(data)

# Split array into 3 equal parts
parts = np.split(arr, 3)

# Print original array
print("Original Array:", arr)

# Print split arrays
print("Split Arrays:")
for part in parts:
    print(part)
