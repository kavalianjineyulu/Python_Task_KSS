# Generator function
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i


# Taking input
n = int(input("Enter a number: "))

# Iterating through generator
for num in generate_numbers(n):
    print(num)
