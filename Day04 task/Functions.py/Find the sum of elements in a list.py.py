def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [10,20,30,40,50]
print("sum:",find_sum(numbers))
