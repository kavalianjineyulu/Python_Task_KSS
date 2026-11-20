import numpy as np

# Temperature data for two days
temperatures = [
    [30, 32, 31],
    [29, 33, 34]
]

# Create a 2D NumPy array
arr = np.array(temperatures)

# Print the array
print("Temperature Data:")
print(arr)

# Find the total temperature
total = np.sum(arr)

print("Total Temperature:", total)
