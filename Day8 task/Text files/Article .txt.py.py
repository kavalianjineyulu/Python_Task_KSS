
# Open the file in read mode
file = open("article.txt", "r")

# Read all contents
content = file.read()

# Count words
words = len(content.split())

# Count lines
file.seek(0)
lines = len(file.readlines())

# Count characters
characters = len(content)

# Display results
print("Number of Words:", words)
print("Number of Lines:", lines)
print("Number of Characters:", characters)

# Close the file
file.close()
