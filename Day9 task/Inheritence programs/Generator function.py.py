
# Generator function
def generate_numbers(N):
    for i in range(1, N + 1):
        yield i


# Taking input
N = int(input("Enter a number: "))

# Calling generator function
for num in generate_numbers(N):
    print(num)
