
# Open the file in read mode
file = open("notes.txt", "r")

# Read all contents from the file
content = file.read()

# Display the contents
print("Daily Notes:")
print(content)

# Close the file
file.close()
