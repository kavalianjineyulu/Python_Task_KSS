num = int(input("enter a number:"))
total = 0
for i in range(1, num):
        if num % i == 0:
            total = total + i
if total == num and num > 0:
    
   print("perfect number")
else:
    print("not a perfect number")
