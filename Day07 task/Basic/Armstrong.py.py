num = int(input("enter a number:"))
temp = num
power = len(str(num))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10
if total == num:
    print("armstrong number")
else:
    print("not an armstrong number")
