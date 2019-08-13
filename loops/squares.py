square_numbers = []

for value in range(1, 11):
    square_number = value**2
    square_numbers.append(square_number)
    
print(square_numbers)

# List comprehension format for the above listing
comprehension_square_numbers = [value**2 for value in range(1, 11)]
print(comprehension_square_numbers)

# Same idea but cubed instead of squared
cubed_numbers = [value**3 for value in range(1, 11)]
print(cubed_numbers)
