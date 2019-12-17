class ModifiedSimplexMethod(object):
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
        pass
    
    def _prompt(self):
        pass
    
    def get_current_solution(self):
        pass
