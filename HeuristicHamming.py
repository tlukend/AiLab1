#inherits to manhattan and hamming
from Heuristic import Heuristic


#Variables: countSteps, runtime(count), memoryEffort(numberOfNodes)

class HeuristicHamming(Heuristic):
    def calculate(self, node, start, goal):
        #this is the distance that the heuristic calculates
        hammingDistance = 0
        for i in range(0, 2):
            for j in range(0, 2):
                if node.state[i][j] != goal[i][j] and node.state[i][j] != 0:
                    hammingDistance += 1
        return hammingDistance


