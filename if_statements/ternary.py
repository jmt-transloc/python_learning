# Ternary operators
order_total = 247

# If/else form
if order_total > 100:
    discount = 25
else:
    discount = 0
print(order_total, discount)

# Ternary form
discount = 25 if order_total > 100 else 0
print(order_total, discount)
