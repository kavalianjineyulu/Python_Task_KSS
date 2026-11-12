numbers = [11, 22, 33, 44, 55]
search = int(input("enter a number to search:"))
for i in numbers:
    if i == search:
        print("number found:",i)
        break
    else:
        print("number not found:",i)
