import numpy as np

# Daily sales of two stores
store_A = [200, 250, 300]
store_B = [180, 270, 310]

# Convert lists into NumPy arrays
arr1 = np.array(store_A)
arr2 = np.array(store_B)

# Find daily difference in sales
difference = arr1 - arr2

# Print the results
print("Store A Sales:", arr1)
print("Store B Sales:", arr2)
print("Daily Sales Difference:", difference)
