if __name__ == "__main__":
    exit()


from Polynomials import *
from functools import lru_cache


class Lagrange:

    def __init__(self, RawX: list, RawY: list):
        self.RawX = list(RawX)
        self.RawY = list(RawY)
        self.Polynomial = list_to_polynomial(self._get_polynomial())
    
    @lru_cache
    def get_value_in_point(self, X: float) -> float:
        return round(eval((' ' + self.Polynomial).replace('x', f'*({X})').replace(' *', ' ').replace('^', '**')), 5)
        # DesiredValue = 0
        # for c in range(len(self.RawY)):
        #     L = self.RawY[c]
        #     for p in range(len(self.RawX)):
        #         if(c != p):
        #             L *= (X - self.RawX[p])/(self.RawX[c] - self.RawX[p])
        #     DesiredValue += L
        # return DesiredValue


    def _get_polynomial(self):
        SUM = [0]
        for c in range(len(self.RawY)):
            pol = [self.RawY[c]]
            for p in range(len(self.RawX)):
                if(c != p):
                    pol = mul_by_num( mul_polynomial( [1, -self.RawX[p]], pol ), 1/(self.RawX[c]-self.RawX[p]) )
            SUM = sum_polynomial(SUM, pol)
        for i, val in enumerate(SUM):
            SUM[i] = round(val, 5)
        return SUM
