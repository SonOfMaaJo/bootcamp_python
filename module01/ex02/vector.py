import sys


class NonMatchedShaped(Exception):
    pass


class Vector:
    def __init__(self, values):
        if type(values) is int:
            self.values = [[float(i)] for i in range(values)]
            self.shape = (1, values)
        elif type(values) is tuple:
            if values[0] > values[1]:
                print("first dimension should less or equal than second.")
                sys.exit(1)
            self.values = [[float(i)] for i in range(values[0], values[1])]
            self.shape = (1, int(values[1] - values[0]))
        elif type(values) is list:
            self.values = values
            self.shape = (len(self.values), 1) if len(self.values) != 1 \
                else (1, len(self.values[0]))
        else:
            raise ValueError('Invalid input.')

    def __add__(self, vector):
        print("add")
        if self.shape != vector.shape:
            raise NonMatchedShaped('shape doesn\'t matche.')
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] +
                            vector.values[0][i]
                            for i in range(self.shape[1])]])
        else:
            return Vector([[self.values[i][0] +
                            vector.values[i][0]]
                           for i in range(self.shape[0])])

    def __radd__(self, vector):
        print("r_add")
        return self.__add__(vector)

    def __sub__(self, vector):
        if self.shape != vector.shape:
            raise NonMatchedShaped('shape doesn\'t matche.')
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] - vector.values[0][i]
                            for i in range(self.shape[1])]])
        else:
            return Vector([[self.values[i][0] - vector.values[i][0]]
                           for i in range(self.shape[0])])

    def __truediv__(self, scalar: float):
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] / scalar
                            for i in range(self.shape[1])]])
        if type(scalar) is not float:
            raise NotImplementedError('division is only possible with scalar')
        else:
            return Vector([[self.values[i][0] / scalar]
                           for i in range(self.shape[0])])

    def __rtruediv__(self, scalar: float):
        raise NotImplementedError('Division of a scalar by a Vector is not '
                                  'defined here.')

    def __mul__(self, scalar: float):
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] * scalar
                            for i in range(self.shape[1])]])
        if type(scalar) is not float and type(scalar) is not int:
            raise NotImplementedError('multiplication is only possible with '
                                      'scalar.')
        else:
            return Vector([[self.values[i][0] * scalar]
                           for i in range(self.shape[0])])

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def __str__(self) -> str:
        return f'{self.values}'

    def __repr__(self) -> str:
        return f'{self.values}'

    def dot(self, vector) -> float:
        if self.shape != vector.shape:
            raise NonMatchedShaped('shapes doesn\'t match.')
        if self.shape[0] == 1:
            return sum([self.values[0][i] * vector.values[0][i]
                        for i in range(self.shape[1])])
        else:
            return sum([self.values[i][0] * vector.values[i][0]
                        for i in range(self.shape[0])])

    def T(self):
        if self.shape[0] == 1:
            return Vector(values=[[self.values[0][i]]
                                  for i in range(self.shape[1])])
        else:
            return Vector(values=[[self.values[i][0]
                                   for i in range(self.shape[0])]])
