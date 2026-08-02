# Name: Navya
# Program: Simple Login Validator

username = "admin"
password = "admin123"

user_name = input("Enter username: ")
user_password = input("Enter password: ")

login_success = (user_name == username) and (user_password == password)

print("Login Successful:", login_success)

# Sample Output 1:
# Enter username: admin
# Enter password: admin123
# Login Successful: True

# Sample Output 2:
# Enter username: navya
# Enter password: 1234
# Login Successful: False