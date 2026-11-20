import time

# Decorator to calculate execution time
def calculate_time(func):
    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()

        execution_time = end_time - start_time

        print("Execution Time:", execution_time, "seconds")

    return wrapper


# Applying decorator
@calculate_time
def my_function():
    time.sleep(2)
    print("Function is executing...")


# Calling function
my_function()
