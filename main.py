if __name__ != "__main__":
    exit()


from Lagrange import Lagrange
from Newton import Newton
from BestSquareMethod import BestSquareMethod
from Polynomials import list_to_polynomial
#from colorama import Fore as fr, init
from modules import *
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt


try:
    RawX = input('Enter X points: ')
    RawX = Dispenser(RawX)
    RawY = input(f'Enter Y points: ')
    RawY = Dispenser(RawY)

    if len(RawX) != len(RawY):
        raise RuntimeError('The number of X points is not equal to the number of Y points')
    
    lg = Lagrange(RawX, RawY)
    nw = Newton(RawX, RawY)
    bs = BestSquareMethod(RawX, RawY)

    print(f'Lagrange polynomial:\n{R}{lg.Polynomial}{X}')
    print(f'Newton polynomial:\n{G}{nw.Polynomial}{X}')
    print(f'Best Square polynimials:')
    for i, polynomial in enumerate(bs.Polynomial):
        print(f'm = {i}: {B}{polynomial}{X}, error: {Y}{acc(bs.get_average_error(i), 5)}{X}')

    interval = get_interval(RawX)

    tbl = PrettyTable()
    tbl.add_column('X values', make_column(lambda x: x, interval))
    tbl.add_column('Lagrange', make_column(lg.get_value_in_point, interval))
    tbl.add_column('Newton',   make_column(nw.get_value_in_point, interval))
    tbl.add_column(f'BSM m: {len(RawX)-1}', make_column(bs.get_value_in_point, interval, len(RawX)-1))
    tbl.add_column(f'BSM m: {round(len(RawX)/2)}', make_column(bs.get_value_in_point, interval, round(len(RawX)/2)))
    tbl.add_column(f'BSM m: {1}', make_column(bs.get_value_in_point, interval, 1))
    print(tbl)

    smooth_interval = np.array([x for x in upped_range(interval[0], interval[-1], 0.01)])
                
    lg_values = np.array([lg.get_value_in_point(x) for x in upped_range(interval[0], interval[-1], 0.01)])
    nw_values = np.array([nw.get_value_in_point(x) for x in upped_range(interval[0], interval[-1], 0.01)])
    bs_values3 = np.array([bs.get_value_in_point(x, 1) for x in upped_range(interval[0], interval[-1], 0.01)])
    bs_values2 = np.array([bs.get_value_in_point(x, round(len(RawX)/2)) for x in upped_range(interval[0], interval[-1], 0.01)])
    bs_values1 = np.array([bs.get_value_in_point(x, len(RawX)-1) for x in upped_range(interval[0], interval[-1], 0.01)])

    lg_core = np.array([lg.get_value_in_point(x) for x in interval])
    nw_core = np.array([nw.get_value_in_point(x) for x in interval])
    bs_core1 = np.array([bs.get_value_in_point(x,len(RawX)-1) for x in interval])
    bs_core2 = np.array([bs.get_value_in_point(x, round(len(RawX)/2)) for x in interval])
    bs_core3 = np.array([bs.get_value_in_point(x, 1) for x in interval])
    core = np.array(interval)

    plt.plot(smooth_interval, lg_values, color='red', label='Lagrange', linestyle='--', lw=3)      #smooth graphic of Lagrange
    plt.plot(smooth_interval, nw_values, color='green', label='Newton', linestyle='-.', lw=2)      #smooth graphic of Newton
    plt.plot(smooth_interval, bs_values3, color='blue', label=f'Best square (m = {1})', linestyle=':', lw=3)   #smooth graphic of Best Square
    plt.plot(smooth_interval, bs_values2, color='blue', label=f'Best square (m = {round(len(RawX)/2)})', linestyle=':', lw=2)
    plt.plot(smooth_interval, bs_values1, color='blue', label=f'Best square (m = {len(RawX)-1})', linestyle=':', lw=1)

    plt.plot(np.array(RawX[:len(RawY)]), np.array(RawY), linestyle='', marker='o', color='red')
    plt.plot(core, lg_core, linestyle='', marker='o', color='black')
    plt.plot(core, nw_core, linestyle='', marker='o', color='black')
    plt.plot(core, bs_core1, linestyle='', marker='o', color='black')
    plt.plot(core, bs_core2, linestyle='', marker='o', color='black')
    plt.plot(core, bs_core3, linestyle='', marker='o', color='black')

    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.title('Comparing Lagrange, Newton and Best Square interpolation methods.')
    plt.show()


except RuntimeError as rm:
    print(f'\n{R}{rm}{X}')
except KeyboardInterrupt:
    print(f'\n{R}Program finished...{X}')
except ValueError:
   print(f'\n{R}Wrong data got{X}')
except:
   print(f'\n{R}Something went wrong{X}')
