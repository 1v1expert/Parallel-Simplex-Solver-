from fractions import Fraction


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
            self._prompt()
    
    def _print_tableau(self):
        pass
    
    def set_simplex_input(self, A, b, c):
        ''' Set initial variables and create tableau.
                '''
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
    
        # If this is a minimization problem...
        if self.prob == 'min':
            # ... find the dual maximum and solve that.
            m = self.get_Ab()
            m.append(self.c + [0])
            m = [list(t) for t in zip(*m)]  # Calculates the transpose
            self.A = [x[:(len(x) - 1)] for x in m]
            self.b = [y[len(y) - 1] for y in m]
            self.c = m[len(m) - 1]
            self.A.pop()
            self.b.pop()
            self.c.pop()
            self.ineq = ['<='] * len(self.b)
    
        # self.create_tableau()
        # self.ineq = ['='] * len(self.b)
        # self.update_enter_depart(self.tableau)
        # self.slack_doc()
        # self.init_tableau_doc()
    
    def _prompt(self):
        pass
    
    def get_current_solution(self):
        pass
