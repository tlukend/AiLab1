from Heuristic import Heuristic



class HeuristicManhattan (Heuristic):
    # Variables: countSteps, runtime(count), memoryEffort(numberOfNodes)
    # stillNotDone

    def findDistance(self, val, goal):
        x1 = y1 = 0

        for i in range (0, 3):
            for j in range (0, 3):
                if goal[i][j] == val:
                    x1 = i
                    y1 = j
                    break

        return x1, y1

    def calculate (self, node, start, goal):
        manhattanDistance = 0
        countSteps = 0
        x1 = x2 = y1 = y2 = 999
        total_h = 0


        for i in range (3):
            for j in range (3):
                x1,y1 = self.findDistance(start[i][j],goal)
                x2,y2 = i,j
                countSteps = abs(x1-x2) + abs(y1-y2)

        return countSteps





