# Pass in a str object, then reverse it
def reverse(str):
    str = ''.join(reversed(str))
    return str

# Using slice notation
def slice_reverse(str):
    str = str[::-1]
    return str

