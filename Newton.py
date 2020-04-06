if __name__ == "__main__":
    exit()


from Polynomials import *
from functools import lru_cache


class Newton:  #class for Newton interpolation
    def __init__(self, RawX: list, RawY: list):  #constructor
        self.RawX = list(RawX)
        self.RawY = list(RawY)
        if(len(self.RawX) != len(self.RawY)):
            raise Exception("Size mismatch")
        self.Polynomial = list_to_polynomial(self._get_polynomial())


    @lru_cache
    def get_value_in_point(self, X: float, Backwards = None) -> float:  #calculates the value in point. 'forward' or 'backwards' calculations are choosed automaticly
        return round(eval((' ' + self.Polynomial).replace('x', f'*({X})').replace(' *', ' ').replace('^', '**')), 5)
        

    def _get_polynomial(self) -> list:  #returns a set of polynomial coefficients
        devided_differences = self._get_devided_differences(False)
        coefficients = self._get_coefficients_for_polynomial(False)
        SUM = [self.RawY[0]]
        for i in range(len(coefficients)):
            SUM = sum_polynomial( SUM, mul_by_num(coefficients[i], devided_differences[i][0]) )
        for i, val in enumerate(SUM):
            SUM[i] = round(val, 5)
        return SUM


    def _get_devided_differences(self, Backwards: bool) -> list:  #calculate of devided differences depending on 'backwards' or 'forward' calculation
        result = list()
        def get_devided_differences(RawX: list, RawY: list, inc = 1) -> None:
            nonlocal result
            result.append([(RawY[i+1] - RawY[i])/(RawX[i+inc]-RawX[i]) for i in range(len(RawX)-inc)])
        get_devided_differences(self.RawX, self.RawY)
        for i in range(1, len(self.RawX)-1):
            get_devided_differences(self.RawX, result[i-1], i+1)
        if Backwards:
            for i in range(len(result)):
                result[i].reverse()
        return result


    def _get_coefficients_for_polynomial(self, Backwards: bool) -> list:
        coefficients = [[1, -self.RawX[0]]] if not Backwards else [[1, self.RawX[-1]]]
        for x in self.RawX[1:-1] if not Backwards else self.RawX[-2:0:-1]:
            coefficients.append(mul_polynomial(coefficients[-1], [1, -x]))
        return coefficients
