from Heuristic import Heuristic



class HeuristicManhattan (Heuristic):
    # Variables: countSteps, runtime(count), memoryEffort(numberOfNodes)
    # stillNotDone


    def find_distance(self, current, goal):
        x1 = y1 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if goal[i][j] == current:
                    x1 = i
                    y1 = j
                    break
        return x1, y1

    def calculate(self, node, current, goal):
        total_h = 0
        x1 = x2 = y1 = y2 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                x1, y1 = self.find_distance(current[i][j], goal)
                x2, y2 = i, j
                tilesteps = abs(x1-x2) + abs(y1-y2)
                total_h += tilesteps

        return total_h





