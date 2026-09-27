def greet(name):
    return "Hello " + name


# (a) Assigning a function to a new variable
new_function = greet

print(new_function("Ravi"))


# (b) Passing a function as an argument
def execute_function(func, name):
    return func(name)

print(execute_function(greet, "Anu"))


# (c) Returning a function from another function
def create_function():
    def message():
        return "Function returned successfully"

    return message


result = create_function()
print(result())
#Hello Ravi
#Hello Anu
#Function returned successfully
