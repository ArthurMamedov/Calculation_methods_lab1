if __name__ == "__main__":
    exit()


from numpy import array, linalg
from Polynomials import *
from math import sqrt
from functools import lru_cache


class BestSquareMethod:
    def __init__(self, RawX, RawY):
        self.RawX = list(RawX)
        self.RawY = list(RawY)
        if(len(self.RawX) != len(self.RawY)):
            raise Exception("Size mismatch")
        self.Polynomial = [list_to_polynomial(self._get_polynomial(m)) for m in range(1, len(RawX) + 1)]


    @staticmethod
    def _degree(X, j):
        for x in X:
            yield x**j


    def _C_j(self, j):
        return sum(self._degree(self.RawX, j))


    def _D_k(self, k):
        return sum([y * x_k for y, x_k in zip(self.RawY, self._degree(self.RawX, k))])


    def _get_polynomial(self, m = None) -> list:
        m = len(self.RawX) if m is None else m
        left_part = array([[self._C_j(i) for i in range(t-m, t)] for t in range(m, 2*m)])
        right_part = array([self._D_k(k) for k in range(m)])
        tmp = list(linalg.solve(left_part, right_part))
        for i, val in enumerate(tmp):
            tmp[i] = round(val, 5)
        tmp.reverse()
        return tmp


    @lru_cache
    def get_value_in_point(self, X, m = 0):
        return round(eval((' ' + self.Polynomial[m]).replace('x', f'*({X})').replace(' *', ' ').replace('^', '**')), 5)


    def get_average_error(self, m = 0):
        tmp = sum((self.RawY[c] - self.get_value_in_point(self.RawX[c], m))**2 for c in range(len(self.RawX)))
        tmp /= len(self.RawX)
        return sqrt(tmp)
