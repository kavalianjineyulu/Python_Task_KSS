import random
import math
numbers = []
for i in range(20):
    num = random.randint(1,200)
    numbers.append(num)
print("random numbers:",numbers)

#calculate maximum value & minimum value
maximum = max(numbers)
minimum = min(numbers)

#calculate sqare root & logarithms
sqrt_value = math.sqrt(maximum)
log_value = math.log(minimum)

 #display the results
print("maximum value:", maximum)
print("minimum value:", minimum)
print("square root of maximum:",sqrt_value)
print("logarithm of minimum:",log_value)
