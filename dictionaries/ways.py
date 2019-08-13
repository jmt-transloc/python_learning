# Ways to build a dictionary in Python
a = dict(A = 1, Z = -1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})

def equality_check():
    return a == b == c == d == e
