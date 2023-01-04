from Heuristic import Heuristic


class HeuristicHamming(Heuristic):
    def calculate(self, node, goal):
        """
        The calculate function figures out the amount of misplaced tiles within the given node by going through the
        two-dimensional array of tiles and comparing them with the goal state tiles
        :param node: the (child-)node needed for this calculation
        :param goal: the goal state needed to be compared with the node
        :return: the function returns an integer of the amount of misplaced tiles
        """
        hamming_distance = 0
        for i in range(0, 3):
            for j in range(0, 3):
                # if current node state is not the same as the goal state or 0
                if node.state[i][j] != goal[i][j] and node.state[i][j] != 0:
                    # we add +1 for the hamming_distance, because it rises the number of misplaced tiles except 0
                    # which is not a tile
                    hamming_distance += 1
                    # return number of misplaced tiles as an integer
        return hamming_distance
