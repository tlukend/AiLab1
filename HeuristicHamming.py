from Heuristic import Heuristic


class HeuristicHamming(Heuristic):
    def calculate(self, node, goal):
        # it counts the wrong states of the puzzle
        # goes through the two-dimensional array
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
