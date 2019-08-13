# Default dictionaries
from collections import defaultdict

default_dictionary = defaultdict(int) # int is the default type

def create_default_in_dic(age):
    default_dictionary['age'] += 1
    return default_dictionary
