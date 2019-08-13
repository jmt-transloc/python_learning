# Named tuples
from collections import namedtuple

Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)

# Calling values by implicit positional reference
vision[0] # Returns 9.5
vision[1] # Returns 8.8

# Calling values by explicit reference
vision.left # Returns 9.5
vision.right # Returns 8.8

# Adding a new name does not interfere with how the values are called
# as named tuples operate by explicit reference and not implicit 
# positional reference
Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)

vision.left # Returns 9.5
vision.right # Returns 8.8
vision.combined # Returns 9.2