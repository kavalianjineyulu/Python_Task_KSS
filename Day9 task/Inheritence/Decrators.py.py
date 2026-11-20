# Authentication decorator
def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            print("User is logged in.")
            func()
        else:
            print("Access Denied! Please login first.")
    return wrapper


# Applying decorator
@login_required
def sensitive_function():
    print("Welcome! You can access sensitive information.")


# Calling function
sensitive_function(True)
sensitive_function(False)
