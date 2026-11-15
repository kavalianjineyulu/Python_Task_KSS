# Open the file in read mode
file = open("article.txt", "r")

# Read all contents
content = file.read()

# Count words, lines and characters
words = len(content.split())
lines = len(content.splitlines())
characters = len(content)

# Display results
print("Total Words:", words)
print("Total Lines:", lines)
print("Total Characters:", characters)

# Close the file
file.close()
