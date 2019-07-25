bicycles = ['trek', 'cannondale', 'raleigh', 'specialized', 'GT']
print(bicycles[1].title())

message = 'My favorite bike company is ' + bicycles[0].title() + '.'

print(message)

# Add a bicycle to the list
bicycles.append('schwinn')

print(bicycles)

# Add a bicycle to the first index, then print
bicycles.insert(0, 'dino')
print(bicycles)

message = 'My favorite bike company is ' + bicycles[0].title() + '.'
print(message)

# Delete the first bicycle
del bicycles[0]
print(bicycles)

# pop() removes the item from a list and allows it to be used unlike del
last_bike = bicycles.pop()
print('The last bike I owned was a ' + last_bike + '.')