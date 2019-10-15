class Matrix:

    def __init__(self, a, b, c, d):
        self.data = [a, b, c, d]

    def __str__(self):
        return '[{}, {}][{}, {}]'.format(self.data[0],
                                         self.data[1],
                                         self.data[2],
                                         self.data[3])

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.data[0] + other.data[0],
                          self.data[1] + other.data[1],
                          self.data[2] + other.data[2],
                          self.data[3] + other.data[3])
        else:
            return NotImplemented


p = Matrix(1, 2, 3, 4)
q = Matrix(5, 6, 7, 8)
r = p + q
print(r)
