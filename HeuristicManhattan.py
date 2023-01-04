from Heuristic import Heuristic


class HeuristicManhattan(Heuristic):

    """
    Manhattan calculates the amount of steps a misplaced tile has to take to reach goal state
    """
    def find_tile_position(self, grid, tile):
        """
        finds the position of the empty tile (x, y)
        :param grid: goal state used to compare with:
        :param tile:value of tile
        :return: if the value of the tile is the same as the value in the grid, return the coordinates
        of this tile back to the calculate function
        """
        for x in range(0, 3):
            for y in range(0, 3):
                if grid[x][y] == tile:
                    return x, y
        return -1, -1

    def calculate(self, node, goal):
        """
        calculates final amount of steps
        :param node: delivers current node, from which we want to calculate the heuristic
        :param goal: the final goal state we need in order to calculate Manhattan Distance
        :return: returns integer of full amount of steps for all tiles (total_h)
        """
        total_h = 0
        for x in range(0, 3):
            for y in range(0, 3):
                tile = node.state[x][y]
                if tile == 0:
                    continue
                x_goal, y_goal = self.find_tile_position(goal, tile)
                total_h += abs(x_goal - x) + abs(y_goal - y)

        return int(total_h)
