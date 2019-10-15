class Person:

    def __init__(self, title, forename, surname):
        self.title = title
        self.forename = forename
        self.surname = surname

    def __str__(self):
        return ' '.join([self.title, self.forename, self.surname])


person = Person('Mr', 'John', 'Smith')
print(person)
