from app import SimplexSolver
from scipy.optimize import linprog
import time

# https://www.kaggle.com/sujoychakma/revised-simplex-implementation-in-python-201736045


class MainTestCase(object):
    def __init__(self):
        self.start_test = time.time()
    
    @staticmethod
    def start(A=[[]], b=[], c=[], method='revised simplex', pprint=False):
        x0_bounds = (0, None)
        x1_bounds = (0, None)
        result = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
                         method=method)
        
        if pprint:
            print(result)

# def test2():
# revised_simplex = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), method='')

# print(result)


case1 = MainTestCase()
case1.start(A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[-2, -45])

SimplexSolver().run_simplex(A=[[2, 1, 0], [1, 2, -2], [0, 1, 2]], b=[10, 20, 5], c=[2, -1, 2])
