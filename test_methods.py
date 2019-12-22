from simplex import SimplexSolver
from modified_simplex import ModifiedSimplexMethod, ModifiedSimplexMethodTwo

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
        
        if self.pprint and result.success:
            print("Current solution: {}, F={}\n".format(result.x, result.fun))
            
        return result

# def test2():
# revised_simplex = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), method='')

# print(result)


# with MainTestCase(pprint=True) as test:
#     """ Maximize(2*X1 + 45*X2)
#     subject to
#     3*x1	+	7*x2	≤	79
#     0*x1    +   5*x2	≤	42
#     -x1     +   0*x2 	≤	-3
#     """
#     result = test.start(A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[-2, -45], method='simplex')
#     if result.success:
#         pass


# SimplexSolver().run_simplex(A=[[2, 1, 0], [1, 2, -2], [0, 1, 2]], b=[10, 20, 5], c=[2, -1, 2])
# ======
# STANDART SOLVER
import multiprocessing as mp

# Step 1: Init multiprocessing.Pool()

# SimplexSolver().run_simplex(
#     A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[2, 45], enable_msg=False, prob='max')


def test_cycle(n):
    ModifiedSimplexMethodTwo().run_simplex(A=[[400, 300], [300, 400], [200, 500]],
                                b=[25000, 27000, 30000],
                                c=[20000, 25000],
                                enable_msg=False,
                                prob='min')

    ModifiedSimplexMethodTwo().run_simplex(A=[[1, 1, 1], [0, 1, 2], [-1, 2, 2]],
                                b=[6, 8, 4],
                                c=[2, 10, 8],
                                enable_msg=False,
                                prob='min')

    ModifiedSimplexMethodTwo().run_simplex(A=[[2, 1], [1, 1]],
                                b=[6, 4],
                                c=[3, 2],
                                enable_msg=False,
                                prob='min')
    return n


pool = mp.Pool(mp.cpu_count())
simplex_start = time.time()
results = [pool.apply(test_cycle, args=(row, )) for row in range(1000)]

# for i in range(1000):
#     test_cycle(i)
print('Full time: {}'.format(time.time() - simplex_start))
# print(results)

# MODIFIED SOLVER
simplex_start = time.time()
test = ModifiedSimplexMethod()
test.run_simplex(
    A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[2, 45], enable_msg=True, prob='max')
# test._print_conditions()
print('Full time: {}'.format(time.time() - simplex_start))

# Simplex solver and checker
# http://simplex.tode.cz/en/#steps

