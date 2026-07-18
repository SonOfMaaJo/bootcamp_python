from math import floor, sqrt


class TinyStatistician(object):
    def __init__(self):
        pass

    def mean(self, x):
        mean = float(sum(x))
        if len(x) == 0:
            return None
        return mean / float(len(x))

    @staticmethod
    def median(x):
        ln = len(x)
        if ln == 0:
            return None
        x = sorted(x)
        return float(x[floor(ln / 2)])

    @staticmethod
    def quartile(x):
        ln = len(x)
        if ln == 0:
            return None
        x = sorted(x)
        return [float(x[floor(ln / 4)]), float(x[floor(3 * ln / 4)])]

    def var(self, x):
        moy = self.mean(x)
        if moy is None:
            return None
        sigma_square = 0
        for el in x:
            sigma_square += (float(el) - float(moy)) ** 2
        return sigma_square / float(len(x))

    def std(self, x):
        sigma_square = self.var(x)
        return sqrt(sigma_square) if sigma_square else None
