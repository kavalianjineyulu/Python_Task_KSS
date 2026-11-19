def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func(is_logged_in)
        else:
            print("access denied! please login first")
    return wrapper
@login_required
def sensitive_function(is_logged_in):
    print("welcome! you can access sensitive information")
sensitive_function(True)
sensitive_function(False)
