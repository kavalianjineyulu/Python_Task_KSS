import numpy as np

# Original list
numbers = [12, 7, 25, 3, 18, 10]

# 1. Convert list into NumPy array
arr = np.array(numbers)

# 2. Sort the array
sorted_arr = np.sort(arr)

# 3. Split the sorted array into two equal parts
parts = np.split(sorted_arr, 2)

# 4. Calculate the sum of each part
sum1 = np.sum(parts[0])
sum2 = np.sum(parts[1])

# Display results
print("Sorted array:", sorted_arr)
print("First split array:", parts[0])
print("Second split array:", parts[1])
print("Sum of first part:", sum1)
print("Sum of second part:", sum2)
