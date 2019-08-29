# Simple addition unit test
def add_one_to_number(number):
    return number + 1

def test_success():
    assert add_one_to_number(4) == 5

def test_failure():
    assert add_one_to_number(2) == 5