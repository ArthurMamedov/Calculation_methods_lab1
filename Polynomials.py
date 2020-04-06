def mul_polynomial(pol1: list, pol2: list) -> list:
    res = [0]*(len(pol1)+len(pol2)-1)
    for i1, val1 in enumerate(pol1):
        for i2, val2 in enumerate(pol2):
            res[i1+i2] += val1*val2
    return res


def mul_by_num(pol: list, num: float) -> list:
    POL = list(pol)
    for i in range(len(POL)):
        POL[i] *= num
    return POL


def sum_polynomial(pol1: list, pol2: list) -> list:
    a = list(pol1); b = list(pol2)
    if len(pol1) > len(pol2):
        b = [0]*(len( pol1 ) - len( pol2 ))
        b.extend(pol2)
    elif len(pol1) < len(pol2):
        a = [0]*(len( pol2 ) - len( pol1 ))
        a.extend(pol1)
    c = [i+j for i, j in zip(a, b)]
    return c

def list_to_polynomial(Coefficients: 'list'):
    '''
    Returns the polynomial in a human language form
    '''
    Formula = str()
    for deg, coef in zip(range(len(Coefficients)-1, -1, -1), Coefficients):
        if coef == 0:
            continue
        elif coef == 1:
            if deg == 0:
                Formula += f'1 '
            elif deg == 1:
                Formula += f'x '
            else:
                Formula += f'x^{deg} '
        else:
            if deg == 0:
                Formula += f'{coef} '
            elif deg == 1:
                Formula += f'{coef}x '
            else:
                Formula += f'{coef}x^{deg} '
    Formula = list(Formula)
    Formula.pop()
    for i in range(len(Formula)-1):
        if Formula[i] == ' ' and Formula[i+1] != '-':
            Formula[i] = '+'
    return ''.join(Formula).replace(' -', ' - ').replace('+', ' + ')