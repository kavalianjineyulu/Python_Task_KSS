import numpy as np

# Original inventory matrix
inventory = [[10, 15],
             [20, 25]]

# Convert into NumPy array
arr = np.array(inventory)

# Add 2 to every element
updated_inventory = arr + 2

# Print the results
print("Original Inventory:")
print(arr)

print("Updated Inventory:")
print(updated_inventory)
