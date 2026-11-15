# Open the file in read mode
file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")
print("----------------")

# Read each line from file
for line in file:
    name, marks = line.split()

    marks = int(marks)

    print(name, marks)

    total = total + marks
    count = count + 1

# Calculate average
if count > 0:
    average = total / count
    print("----------------")
    print("Total Marks:", total)
    print("Average Marks:", average)
else:
    print("No student records found.")

# Close the file
file.close()
