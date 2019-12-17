from app import SimplexSolver
from scipy.optimize import linprog
import time

SimplexSolver().run_simplex([[2, 1, 0],
                             [1, 2, -2],
                             [0, 1, 2]],
                            [10, 20, 5],
                            [2, -1, 2])

# https://www.kaggle.com/sujoychakma/revised-simplex-implementation-in-python-201736045



class Test1(object):
    def __init__(self):
        self.start_test = time.time()
    
    def start(self, method='revised simplex', pprint=False):
        x0_bounds = (0, None)
        x1_bounds = (0, None)
        result = linprog([-2, -45], A_ub=[[3, 7], [0, 5], [-1, 0]], b_ub=[79, 42, -3], bounds=(x0_bounds, x1_bounds),
                         method=method)

# def test2():
# revised_simplex = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), method='')

# print(result)

Test1().start()