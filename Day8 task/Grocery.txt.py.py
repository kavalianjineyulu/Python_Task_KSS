# Open file in write mode
file = open("grocery.txt", "w")

# Get number of items
n = int(input("How many grocery items? "))

# Take items from user
for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")

# Close the file
file.close()

print("\nGrocery items saved successfully!")
