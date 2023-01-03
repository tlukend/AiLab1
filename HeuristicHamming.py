from Heuristic import Heuristic

class HeuristicHamming(Heuristic):
    def calculate(self, node, start, goal):
        #it counts the wrong states of the puzzle
        hammingDistance = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if node.state[i][j] != goal[i][j] and node.state[i][j] != 0:
                    hammingDistance += 1
        return hammingDistance


