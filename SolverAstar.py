from Solver import Solver
from Node import Node

"""Inherits from Solver. The SolverAstar class contains the solve function, which takes a random start state from 
puzzle and returns the node with the goal state. This is where the A-Star algorithm is implemented. A Object of 
SolverAstar takes a heuristic as input parameter. This can be the hamming or the manhattan heuristic. Thanks to the 
modular design the SolverAstar can use any given heuristic. """


class SolverAstar(Solver):
    def __init__(self, heuristic):
        self.heuristic = heuristic

        """The function takes a random start state and a designated goal state and returns the goal state and the 
        number of expanded nodes. To solve the puzzle it uses the Astar algorithm. To calculate the total costs it 
        uses a heuristic (hamming or manhattan). """

    def solve(self, puzzle):
        """
        this is our queue - open nodes are only visited
        """
        open_nodes = []
        """
        set() to have access time O(1)
        """
        open_nodes_set = set()
        """
        closed nodes is a visited and expanded node
        """
        closed_nodes_set = set()
        """
        start_node is our start_state puzzle and also uses the depth which is 0 at the beginning
        """
        start_node = Node(puzzle.start_state, 0)
        """
        to calculate the costs with Manhattan or Hamming
        """
        start_node.update_heuristic(self.heuristic.calculate(start_node, puzzle.grid_goal))
        """
        node is visited but not expanded - we give it in list and set
        """
        open_nodes.append(start_node)
        open_nodes_set.add(start_node)

        """
        Just for Testing:
        print(puzzle.start_state)
        print('open_nodes_set: ')
        for i in open_nodes_set:
            print(i.state)
        """

        while len(open_nodes) != 0:
            current_node = open_nodes.pop(0)
            open_nodes_set.remove(current_node)
            if current_node.state == puzzle.grid_goal:
                """
                 returns the solved current node (which is the same as goal_state now) and the numbers of expanded
                 nodes (we give all expanded nodes in closed_nodes_set)
                """
                return current_node, (len(closed_nodes_set) + len(open_nodes))
            else:
                closed_nodes_set.add(current_node)
                child_nodes = current_node.generate_child_states()

                """
                for testing
                print('Prints Child nodes of Depth ')
                for i in child_nodes:
                    print('depth ' + str(i.depth))
                    grid.print_grid(i.state)
                """
                """
                search for a suitable child node which is 'unused' (not visited and also not expanded)
                """
                for child in child_nodes:
                    if child in open_nodes_set or child in closed_nodes_set:
                        """
                        no suitable child node -> therefore continue to get the net node to check if suitable
                        """
                        continue
                    else:
                        """
                        the child node is suitable and added to the open_nodes_set (therefore it is visited)
                        """
                        child.update_heuristic(self.heuristic.calculate(child, puzzle.grid_goal))
                        open_nodes_set.add(child)

                        """
                        for testing
                        print('child.total_costs: ')
                        print(child.total_costs())
                        """
                        """position for the child node - a inexpensive alternative to sorting a list - least 
                        expensive element is put on index 0 """
                        target_node_index = 0
                        for node in open_nodes:
                            if node.total_cost > child.total_cost:
                                break
                            else:
                                """
                                for position of the child in the queue open_node - if not on the position 0 / first
                                position
                                """
                                target_node_index += 1
                        open_nodes.insert(target_node_index, child)
        return "Unable to solve!"
