import HeuristicHamming
import Solver
import Node
import grid
import Heuristic
class SolverAstar(Solver):
    def __init__(self, heuristic):
        self.heuristic = heuristic
    def solve(self, puzzle):

        #visited but not expanded
        open_nodes = []
        #visited and expanded
        closed_nodes = []
        start_state = grid.create_random_grid()
        # f(n) = g(n) + h(n), f(n) = total_cost, g(n) = current_cost, h(n) = heuristic.calculate()
        current_cost = 0
        total_cost = current_cost + HeuristicHamming.calculate()
        start_node =  Node(start_state, total_cost)
        open_nodes.append(start_node)
        while open_nodes != None:
            current_node = open_nodes.sort(reverse = False, key = lambda node: node.total_cost)




