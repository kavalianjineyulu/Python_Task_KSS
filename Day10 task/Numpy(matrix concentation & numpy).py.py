import numpy as np

# Branch A employee data
branch_A = [[10, 20],
            [30, 40]]

# Branch B employee data
branch_B = [[5, 15],
            [25, 35]]

# Convert into NumPy arrays
arr1 = np.array(branch_A)
arr2 = np.array(branch_B)

# Combine both matrices vertically
combined = np.concatenate((arr1, arr2), axis=0)

# Calculate total employees
total = np.sum(combined)

# Print the results
print("Combined Matrix:")
print(combined)

print("Total Employees:", total)
