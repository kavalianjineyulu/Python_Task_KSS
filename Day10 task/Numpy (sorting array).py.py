import numpy as np

# Product prices
prices = [499, 299, 799, 199, 599]

# Convert list into NumPy array
arr = np.array(prices)

# Sort prices in ascending order
sorted_prices = np.sort(arr)

# Print the results
print("Original Prices:", arr)
print("Sorted Prices:", sorted_prices)
