from Heuristic import Heuristic


class HeuristicManhattan(Heuristic):
    # Variables: countSteps, runtime(count), memoryEffort(numberOfNodes)
    # stillNotDone

    def find_tile_position(self, grid, tile):
        for x in range(0, 3):
            for y in range(0, 3):
                if grid[x][y] == tile:
                    return x, y
        return -1, -1

    def calculate(self, node, goal):
        total_h = 0
        for x in range(0, 3):
            for y in range(0, 3):
                tile = node.state[x][y]
                if tile == 0:
                    continue
                x_goal, y_goal = self.find_tile_position(goal, tile)
                total_h += abs(x_goal - x) + abs(y_goal - y)
        """
        for testing:
        print('Total h: ' + str(total_h))
        """
        return int(total_h)
