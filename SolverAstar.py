from Solver import Solver
from Node import Node

class SolverAstar(Solver):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, puzzle):
        # this is our queue
        open_nodes = []
        # set() to have access time O(1)
        open_nodes_set = set()
        closed_nodes_set = set()
        # start_node is our start_state puzzle and also uses the depth which is 0 at the beginning
        start_node = Node(puzzle.start_state, 0)
        # to calculate the costs with Manhattan or Hamming
        start_node.heuristic = self.heuristic.calculate(start_node, puzzle.start_state, puzzle.grid_goal)

        # node is visited but not expanded - we give it in list and set
        open_nodes.append(start_node)
        open_nodes_set.add(start_node)

        while len(open_nodes) != 0:
            current_node = open_nodes.pop(0)
            open_nodes_set.remove(current_node)
            if current_node.state == puzzle.grid_goal:
                # returns the goal_state - because is solved
                return current_node
            else:
                closed_nodes_set.add(current_node)
                child_nodes = current_node.generate_child_states()

                # search for a suitable child node which is 'unused' (not visited)
                for child in child_nodes:
                    if child in open_nodes_set or child in closed_nodes_set:
                        # no suitable child node -> therefore continue to get the net node to check if suitable
                        continue
                    else:
                        # the child node is suitable and added to the open_nodes_set (therefore it is visited)
                        child.heuristic = self.heuristic.calculate(child, puzzle.start_state, puzzle.grid_goal)
                        open_nodes_set.add(child)
                        #
                        target_node_index = 0
                        for node in open_nodes:
                            if node.total_costs() > child.total_costs():
                                break
                            else:
                                target_node_index += 1
                        open_nodes.insert(target_node_index, child)
        return "Unable to solve!"