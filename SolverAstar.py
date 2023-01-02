from Solver import Solver

class SolverAstar(Solver):
    def __init__(self, heuristic):
        self.heuristic = heuristic
    def solve(self, puzzle):
        #TODO: hier kommt der Algorithmus rein (Slavica)