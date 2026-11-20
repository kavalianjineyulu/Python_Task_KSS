
# Take student name as input
name = input("Enter student name: ")

# Open file in append mode
file = open("attendance.txt", "a")

# Write student name into the file
file.write(name + "\n")

# Close the file
file.close()

# Open file in read mode
file = open("attendance.txt", "r")

# Display file contents
print("\nStudent Attendance:")
print(file.read())

# Close the file
file.close()
