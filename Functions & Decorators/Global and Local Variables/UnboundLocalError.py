counter = 0

def modify_counter():
    counter += 1

try:
    modify_counter()
except UnboundLocalError as e:
    print("Error:", e)

def modify_counter_fixed():
    global counter
    counter += 1

modify_counter_fixed()
print("Counter after fixing:", counter)
#Error: cannot access local variable 'counter' where it is not associated with a value
#Counter after fixing: 1
