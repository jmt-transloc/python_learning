# Using for loops to print pairs of lists
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]

# This can be done better as it is using implicit positional
# referencing to grab age
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

# This is the more Pythonic version using explicit referencing
for person, age in zip(people, ages):
    print(person, age)
