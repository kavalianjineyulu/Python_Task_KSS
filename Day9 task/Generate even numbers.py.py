def even_numbers():
    num = 2
    while True:
        yield num
        num += 2
n = int(input("enter how many even numbers:"))
gen = even_numbers()
for i in range(n):
    print(next(gen))
