from fractions import Fraction
import copy

import numpy as np

from simplex import SimplexSolver


class ModifiedSimplexMethodTwo(SimplexSolver):
    def run_simplex(self, A=[[]], b=[], c=[], prob='max', ineq=list(), enable_msg=False, latex=True):
        """ Run simplex algorithm. """
        self.prob = prob
        self.gen_doc = latex
        self.ineq = ineq
        
        # Create the header for the latex doc.
        # self.start_doc()
        
        # Add slack & artificial variables
        self.set_simplex_input(A, b, c)
        
        # Are there any negative elements on the bottom (disregarding
        # right-most element...)
        while not self.should_terminate():
            # ... if so, continue.
            if enable_msg:
                # clear()
                self._print_tableau()
                print("Current solution: %s\n" %
                      str(self.get_current_solution()))
                self._prompt()
            
            # Attempt to find a non-negative pivot.
            pivot = self.find_pivot()
            if pivot[1] < 0:
                if enable_msg:
                    print("There exists no non-negative pivot. "
                          "Thus, the solution is infeasible.")
                # self.infeasible_doc()
                # self.print_doc()
                return None
            else:
                # self.pivot_doc(pivot)
                if enable_msg:
                    # clear()
                    self._print_tableau()
                    print("\nThere are negative elements in the bottom row, "
                          "so the current solution is not optimal. "
                          "Thus, pivot to improve the current solution. The "
                          "entering variable is %s and the departing "
                          "variable is %s.\n" %
                          (str(self.entering[pivot[0]]),
                           str(self.departing[pivot[1]])))
                    self._prompt()
                    print("\nPerform elementary row operations until the "
                          "pivot is one and all other elements in the "
                          "entering column are zero.\n")
            
            # Do row operations to make every other element in column zero.
            self.pivot(pivot)
            # self.tableau_doc()
        
        solution = self.get_current_solution()
        # self.final_solution_doc(solution)
        if enable_msg:
            # clear()
            self._print_tableau()
        
        # print("Current solution: %s\n" % str(solution))
        # print("That's all folks!")
        
        # self.print_doc()
        return solution


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

