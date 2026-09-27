from functools import wraps

is_logged_in = True


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")

    return wrapper


@require_login
def view_profile():
    print("Welcome to your profile!")


print("When user is logged in:")
is_logged_in = True
view_profile()


print("\nWhen user is not logged in:")
is_logged_in = False
view_profile()
#When user is logged in:
#Welcome to your profile!

#When user is not logged in:
#Access denied. Please log in.
