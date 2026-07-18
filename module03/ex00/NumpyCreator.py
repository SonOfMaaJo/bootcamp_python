import numpy as np
from random import random


class NumpyCreator(object):
    def from_list(self, lst, dtype=None):
        try:
            if not isinstance(lst, list):
                return None
            array = np.array(lst, dtype=dtype)
            return array
        except Exception:
            return None

    def from_tuple(self, tpl, dtype=None):
        try:
            if not isinstance(tpl, tuple):
                return None
            return np.array(tpl, dtype=dtype)
        except Exception:
            return None

    def from_iterable(self, itr, dtype=None):
        try:
            return np.array(itr, dtype=dtype)
        except Exception:
            return None

    def from_shape(self, shape, value=0, dtype=None):
        try:
            if not isinstance(shape, tuple):
                return None
            return np.array([[value for i in range(shape[1])]
                             for j in range(shape[0])], dtype=dtype)
        except Exception as e:
            return None

    def random(self, shape, dtype=None):
        try:
            if not isinstance(shape, tuple):
                return None
            return np.array([[random() for i in range(shape[1])]
                             for j in range(shape[0])], dtype=dtype)
        except Exception:
            return None

    def identity(self, n, dtype=None):
        try:
            if not isinstance(n, int):
                return None
            return np.identity(n, dtype=dtype)
        except Exception:
            return None
