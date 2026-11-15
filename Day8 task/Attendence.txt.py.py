# Take student name from user
name = input("Enter student name: ")

# Append student name to file
file = open("attendance.txt", "a")
file.write(name + "\n")
file.close()

# Display file contents
file = open("attendance.txt", "r")

print("\nStudent Attendance:")
print(file.read())

file.close()
