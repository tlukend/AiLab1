import grid
from Solver import Solver
from Node import Node


class SolverAstar(Solver):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, puzzle):
        open_nodes = []
        open_nodes_set = set()
        closed_nodes_set = set()
        start_node = Node(puzzle.start_state, 0)
        start_node.heuristic = self.heuristic.calculate(start_node, puzzle.start_state, puzzle.grid_goal)
        open_nodes.append(start_node)
        open_nodes_set.add(start_node)
        while len(open_nodes) != 0:
            current_node = open_nodes.pop(0)
            open_nodes_set.remove(current_node)
            if current_node.state == puzzle.grid_goal:
                return current_node
            else:
                closed_nodes_set.add(current_node)
                child_nodes = current_node.generate_child_states()
                for child in child_nodes:
                    if child in open_nodes_set or child in closed_nodes_set:
                        continue
                    else:
                        child.heuristic = self.heuristic.calculate(child, puzzle.start_state, puzzle.grid_goal)
                        open_nodes_set.add(child)
                        target_node_index = 0
                        for node in open_nodes:
                            if node.total_costs() > child.total_costs():
                                break
                            else:
                                target_node_index += 1
                        open_nodes.insert(target_node_index, child)
        return "Unable to solve!"


# f(n) = g(n) + h(n), f(n) = total_cost, g(n) = current_cost, h(n) = heuristic.calculate()

