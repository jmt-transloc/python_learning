# Break statements
items = [0, None, 0.0, True, 0, 7]
found = False # Setting a 'flag'

for item in items:
    print('Scanning item', item)
    if item:
        found = True # Update the flag
        break      

if found: # Inspect the flag
    print('At least one item evaluates as True')
else:
    print('All items evaluate to False')
