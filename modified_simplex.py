from fractions import Fraction
import copy

import numpy as np


class ModifiedSimplexMethod(object):
    def __init__(self):
        self.A = []
        self.b = []
        self.c = []
        self.tableau = []
        self.entering = []
        self.departing = []
        self.ineq = []
        self.prob = "max"
        self.gen_doc = False
        self.doc = ""
        
    def run_simplex(self, A=[[]], b=[], c=[], prob='max', ineq=list(), enable_msg=False, latex=True):
        """ Run simplex algorithm. """
        
        # Add slack & artificial variables
        self.set_simplex_input(A, b, c)
        
        if enable_msg:
            # clear()
            self._print_tableau()
            print("Current solution: %s\n" %
                  str(self.get_current_solution()))
            # self._prompt()
    
    def _print_tableau(self):
        """ Print simplex tableau. """
        output = ' '
        for val in self.entering:
            output += '{:^5}'.format(str(val))
        print(output + ' ')
        
        output = ''
        for num, row in enumerate(self.tableau):
            output += '|'
        
            for index, val in enumerate(row):
                output += '{:^5}'.format(str(val))
            if num < (len(self.tableau) - 1):
                output += '| %s' % self.departing[num]
            else:
                output += '|'
            output += '\n'
        print(output)
    
    def set_simplex_input(self, A, b, c) -> None:
        """ Set initial variables and create tableau. """
        # Convert all entries to fractions for readability.
        for a in A:
            self.A.append([Fraction(x) for x in a])
        self.b = [Fraction(x) for x in b]
        self.c = [Fraction(x) for x in c]
        if not self.ineq:
            if self.prob == 'max':
                self.ineq = ['<='] * len(b)
            elif self.prob == 'min':
                self.ineq = ['>='] * len(b)
    
        self.update_enter_depart(self.get_Ab())
        # self.init_problem_doc()
    
        self.create_tableau()
        # self.ineq = ['='] * len(self.b)
        self.update_enter_depart(self.tableau)
        # self.slack_doc()
        # self.init_tableau_doc()
    
    def _print_conditions(self):
        func = ''
        for i, x in enumerate(self.c):
            func += '+{}X{}'.format(x, i)
        print("Func {}({})".format(self.prob, func))
    
    def get_current_solution(self):
        pass

    def get_Ab(self):
        """ Get A matrix with b vector appended. """
    
        matrix = copy.deepcopy(self.A)
        for i in range(0, len(matrix)):
            matrix[i] += [self.b[i]]
        return matrix
    
    def create_tableau(self):
        """ Create initial tableau table."""

        self.tableau = copy.deepcopy(self.A)
        self.add_slack_variables()
        c = copy.deepcopy(self.c)
        for index, value in enumerate(c):
            c[index] = -value
        self.tableau.append(c + [0] * (len(self.b) + 1))
        
    def add_slack_variables(self):
        """ Add slack & artificial variables to matrix A to transform
            all inequalities to equalities.
        """
        slack_vars = self._generate_identity(len(self.tableau))
        # print(slack_vars)
        # print(slack_vars[0], self.tableau)
        for i in range(0, len(slack_vars)):
            self.tableau[i] += slack_vars[i]
            self.tableau[i] += [self.b[i]]
    
    @staticmethod
    def _generate_identity(n: int) -> np.ndarray:
        """ Helper function for generating a square identity matrix. """
        I = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            I.append(row)
        return I
    
    def update_enter_depart(self, matrix):
        self.entering = []
        self.departing = []
        # Create tables for entering and departing variables
        for i in range(0, len(matrix[0])):
            if i < len(self.A[0]):
                prefix = 'x' if self.prob == 'max' else 'y'
                self.entering.append("%s_%s" % (prefix, str(i + 1)))
            elif i < len(matrix[0]) - 1:
                self.entering.append("s_%s" % str(i + 1 - len(self.A[0])))
                self.departing.append("s_%s" % str(i + 1 - len(self.A[0])))
            else:
                self.entering.append("b")

# import time
#
# simplex_start = time.time()
# test = ModifiedSimplexMethod()
# test.run_simplex(
#     A=[[3, 7], [0, 5], [-1, 0]], b=[79, 42, -3], c=[2, 45], enable_msg=True, prob='max')
# test._print_conditions()
# print('Full time: {}'.format(time.time() - simplex_start))