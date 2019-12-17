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
        print(' ')
        for val in self.entering:
            print('{:^5}'.format(str(val)))
        print(' ')
        for num, row in enumerate(self.tableau):
            print('|')
        
            for index, val in enumerate(row):
                print('{:^5}'.format(str(val)))
            if num < (len(self.tableau) - 1):
                print('| %s' % self.departing[num])
            else:
                print('|')
    
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
    
        # self.update_enter_depart(self.get_Ab())
        # self.init_problem_doc()
    
        # self.create_tableau()
        # self.ineq = ['='] * len(self.b)
        # self.update_enter_depart(self.tableau)
        # self.slack_doc()
        # self.init_tableau_doc()
    
    def _print_conditions(self):
        func = ''
        for i, x in enumerate(self.c):
            func += '+{}X{}'.format(x, i)
        print("Func {}({})".format(self.prob, func))
    
    def get_current_solution(self):
        pass
    
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
        for i in range(0, len(slack_vars)):
            self.tableau[i] += slack_vars[i]
            self.tableau[i] += [self.b[i]]
    
    @staticmethod
    def _generate_identity(n: int) -> np.ndarray:
        """ Helper function for generating a square identity matrix. """
        return np.eye(n)
