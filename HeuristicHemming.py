#inherits to manhattan and hemming
from Heuristic import Heuristic


#Variables: countSteps, runtime(count), memoryEffort(numberOfNodes)

class HeuristicHemming(Heuristic):
    def calculate(self, node, start, goal):
        #this is the distance that the heuristic calculates
        hemmingDistance = 0
        for i in range(0, 2):
            for j in range(0, 2):
                if node.state[i][j] != goal[i][j] and node.state[i][j] != '_':
                    hemmingDistance += 1
        return hemmingDistance


