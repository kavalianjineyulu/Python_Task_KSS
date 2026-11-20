import numpy as np

# Sensor readings
sensor1 = [10, 20, 30]
sensor2 = [40, 50, 60]

# Convert lists into NumPy arrays
arr1 = np.array(sensor1)
arr2 = np.array(sensor2)

# Combine both arrays using concatenation
combined = np.concatenate((arr1, arr2))

# Print the results
print("Sensor 1 Readings:", arr1)
print("Sensor 2 Readings:", arr2)
print("Combined Array:", combined)
