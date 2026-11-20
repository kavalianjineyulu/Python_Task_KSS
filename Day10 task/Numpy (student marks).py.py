import numpy as np

# Original marks
marks = [45, 67, 89, 56, 72]

# Convert list into NumPy array
arr = np.array(marks)

# Add 5 grace marks to every student
updated_marks = arr + 5

# Print updated marks
print("Original Marks:", arr)
print("Updated Marks:", updated_marks)
