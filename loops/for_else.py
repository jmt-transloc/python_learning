# Else statements following for and while
class DriverException(Exception):
    pass

people = [('James', 17), ('Kirk', 9), ('Laris', 13), ('Robert', 8)]
# driver = None

# for person, age in people:
#     if age >= 18:
#         driver = (person, age)
#         break

# if driver is None:
#     raise DriverException('Driver not found.')

# The above can be re-written in a more Pythonic way
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:
    raise DriverException('Driver not found.')