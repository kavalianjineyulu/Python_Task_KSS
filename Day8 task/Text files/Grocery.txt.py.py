
# Open file in write mode
file = open("grocery.txt", "w")

# Get number of items
n = int(input("How many grocery items do you want to enter? "))

# Take multiple items from user
for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")

# Close the file
file.close()

print("Grocery items saved successfully!")

# Display file contents
file = open("grocery.txt", "r")

print("\nGrocery Items:")
print(file.read())

file.close()
