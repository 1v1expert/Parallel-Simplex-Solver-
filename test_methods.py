from app import SimplexSolver
from scipy.optimize import linprog
import time

# https://www.kaggle.com/sujoychakma/revised-simplex-implementation-in-python-201736045


class MainTestCase(object):
    def __init__(self, pprint=False):
        self.pprint = pprint
        self.start_test = time.time()
        self.x0_bounds = (0, None)
        self.x1_bounds = (0, None)
        
    def __enter__(self):
        return self
        # return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.pprint:
            print('Full time: {}'.format(time.time() - self.start_test))
        return False
    
    def start(self, A=[[]], b=[], c=[], method='revised simplex'):

        result = linprog(c, A_ub=A, b_ub=b, bounds=(self.x0_bounds, self.x1_bounds), method=method)
        
        if self.pprint:
            print(result)
            
        return result

# def test2():
# revised_simplex = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), method='')

# print(result)


with MainTestCase(pprint=True) as test:
    """ Maximize(2*X1 + 45*X2)
    subject to
    3*x1	+	7*x2	≤	79
    0*x1    +   5*x2	≤	42
    -x1     +   0*x2 	≤	-3
    """
    result = test.start(A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[-2, -45])
    if result.success:
        print(result.x)
    

# SimplexSolver().run_simplex(A=[[2, 1, 0], [1, 2, -2], [0, 1, 2]], b=[10, 20, 5], c=[2, -1, 2])
# SimplexSolver().run_simplex(A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[-2, -45])

