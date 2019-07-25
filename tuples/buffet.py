foods = ('pasta', 'fish', 'steak', 'chicken', 'pork')

for food in foods:
    print('We offer ' + food + '.')

# Tuples should result in an error when attempting to append
# foods.append('caviar')

# Since tuples are immutable, we must 'overwrite' the existing tuple
# This is similar to lists in Clojure
foods = ('pasta', 'fish', 'soup', 'chicken', 'caviar')

for food in foods:
    print('We offer ' + food + '.')