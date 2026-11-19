import time
def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print("execution time:",execution_time,"seconds")
    return wrapper
@calculate_time
def my_function():
    time.sleep(2)
    print("function is running...")
my_function()
