from colorama import init, Fore as fr
init()


R = fr.LIGHTRED_EX
G = fr.LIGHTGREEN_EX
B = fr.LIGHTBLUE_EX
X = fr.RESET
Y = fr.LIGHTYELLOW_EX
acc = '{:.7f}'.format

def make_column(function, interval, m = None):
    column = []
    for x in interval:
        if m is None:
            column.append(function(x))
        else:
            column.append(function(x, m))
    return column


def Dispenser(tmp: 'str'):
    '''
    Splits the string to a list of floats
    '''
    if(type(tmp) is not str):
        raise TypeError
    array = tmp.split()
    for c in range(len(array)):
        array[c] = float(array[c])
    return array


def upped_range(start, finish, step = 1):
    while start < finish:
        yield start
        start += step


def get_interval(Points: list) -> list:
    interval = [Points[0] - (Points[1] - Points[0])/2]
    try:
        for i in range(len(Points)):
            interval.append(Points[i])
            interval.append(Points[i] + (Points[i+1] - Points[i])/2)
    except IndexError:
        pass
    interval.append(Points[-1] + (Points[-1] - Points[-2])/2)
    return interval