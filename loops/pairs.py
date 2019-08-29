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

# Adding nationalities for more pairing
nationalities = ['Belgium', 'Spain', 'England', 'Ireland']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

# Exploding the tuple returned by our loop
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)

# Using a while loop in place of a for loop (don't do this)
#
# This code simulates a for loop by covering initialization, condition,
# and updating the variable 'position'
position = 0 # Initialization
while position < len(people): # Condition
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1 # Update
