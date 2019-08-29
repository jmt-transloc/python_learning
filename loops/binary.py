# While loops to determine binary numbers
n = 39
remainders = []

while n > 0:
    remainder = n % 2 # Remainder of division by 2
    remainders.append(remainder) # Save the remainders
    n //= 2 # Divide n by 2

remainders = remainders[::-1]
print(remainders)

# The above can be more Pythonic using divmod
while n > 0:
    n, remainder = divmod(n, 2) # Divmod uses a number and divisor
    remainders.append(remainder)

remainders = remainders[::-1]
print(remainders)
