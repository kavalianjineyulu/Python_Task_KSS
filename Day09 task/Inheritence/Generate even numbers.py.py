
def even_numbers():
    num = 2
    while True:
        yield num
        num += 2


# Get input from user
N = int(input("Enter how many even numbers to print: "))

# Create generator object
gen = even_numbers()

# Print first N even numbers
for i in range(N):
    print(next(gen))
