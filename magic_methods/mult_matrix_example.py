class Matrix:

    def __init__(self, a, b, c, d):
        self.data = [a, b, c, d]

    def __str__(self):
        return '[{}, {}][{}, {}]'.format(self.data[0],
                                         self.data[1],
                                         self.data[2],
                                         self.data[3])

    def __mul__(self, other):
        """
        __mul__ expects the following
        :self - A Matrix
        :other - An int
        """
        if isinstance(other, (int, float)):
            return Matrix(self.data[0] * other,
                          self.data[1] * other,
                          self.data[2] * other,
                          self.data[3] * other)
        elif isinstance(other, Matrix):
            return Matrix(self.data[0] * other.data[0] + self.data[1] * other.data[1],
                          self.data[0] * other.data[1] + self.data[1] * other.data[3],
                          self.data[2] * other.data[0] + self.data[3] * other.data[1],
                          self.data[2] * other.data[1] + self.data[3] * other.data[3])
        else:
            return NotImplemented

    def __rmul__(self, other):
        """
        __rmul__ reverses the arguments so that :self is a int and :other is a Matrix
        whereas __mul__ expects :self to be a Matrix and :other to be an int
        This prevents input failure due to reversed params
        """
        if isinstance(other, (int, float)):
            return Matrix(self.data[0] * other,
                          self.data[1] * other,
                          self.data[2] * other,
                          self.data[3] * other)
        else:
            return NotImplemented


p = Matrix(1, 2, 3, 4)
q = Matrix(2, 4, 6, 8)
print(2*p)
print(p*q)
