def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price


print("Only Price:", calculate_price(1000))

print("Price and Custom Tax:", calculate_price(1000, 10))

print("All Arguments:", calculate_price(1000, 10, 100))
#Only Price: 1180.0
#Price and Custom Tax: 1100.0
#All Arguments: 1000.0
