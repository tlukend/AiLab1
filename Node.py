import Constants
from Grid import swap_cells


class Node:
    """The constructor accepts a 2 dimensional array in which the state of the grid is saved
     If no parent is passed, parent is set to none
     """
    def __init__(self, state, depth, parent=None):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.heuristic = 0
        self.total_cost = depth
        self.hash = 0
        self.calculate_hash()

    """To generate a unique number for the builtin hash function"""
    def calculate_hash(self):
        self.hash = 0
        i = 0
        for column in self.state:
            for number in column:
                """Xor operation. We use bit shifting: number is shifted by three bits to 
                the left """
                self.hash ^= number << (3 * i)
                i += 1

    def update_heuristic(self, heuristic):
        self.heuristic = heuristic
        """
        calculates the total costs for a node
        no input parameters
        :return: the total costs: f(n) = g(n) + h(n), f(n) = total_cost, g(n) = depth, h(n) = heuristic.calculate()
        """
        self.total_cost = self.depth + self.heuristic

    """We override the builtin hash function, to return our own generated hash. We will need this for the set - 
    access time for datatype set is O(1) """
    def __hash__(self):
        return self.hash

    """compares two objects/states by there values. The function was optimized with loop unrolling. Instead looping 
    we manually compare the cells """
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.state[0][0] != other.state[0][0]:
            return False
        if self.state[0][1] != other.state[0][1]:
            return False
        if self.state[0][2] != other.state[0][2]:
            return False
        if self.state[1][0] != other.state[1][0]:
            return False
        if self.state[1][1] != other.state[1][1]:
            return False
        if self.state[1][2] != other.state[1][2]:
            return False
        if self.state[2][0] != other.state[2][0]:
            return False
        if self.state[2][1] != other.state[2][1]:
            return False
        if self.state[2][2] != other.state[2][2]:
            return False
        return True

    @staticmethod
    def is_inside_grid(x, y):
        """
        checks if the position (if we move the empty tile) is inside the grid
        :param x: x coordinate (of array) -> is between 0 and 2
        :param y: x coordinate (of array) -> is between 0 and 2
        :return: True if grid is inside - False if grid is not inside and x or y > 2 is
        """
        return 0 <= x <= 2 and 0 <= y <= 2

    def get_number_at(self, x, y):
        """
        this functions provides the number of the position in the grid
        :param x: x coordinate (of array) -> is between 0 and 2
        :param y: x coordinate (of array) -> is between 0 and 2
        :return: returns the number if x and y are inside the grid
        """
        if not self.is_inside_grid(x, y):
            return None
        else:
            return self.state[x][y]

    def get_empty_tile(self):
        """
        this function looks for the empty tile and returns the position/coordinates
        no input
        :return: x and y (the coordinate)
        """
        for x in range(0, 3):
            for y in range(0, 3):
                if self.state[x][y] == 0:
                    return x, y

    def generate_child_states(self):
        """
        this function creates all possible children: it moves the empty style in all possible directions and creates
        a new state (child)
        no input
        :return: all created children
        """
        children = []
        # coordinates of the empty tiles
        empty_tile = self.get_empty_tile()
        # child states are generated - for each direction
        for direction in Constants.DIRECTIONS:
            # vector addition to get the new grid which we can move
            x = empty_tile[0]+direction[0]
            y = empty_tile[1]+direction[1]
            if not self.is_inside_grid(x, y):
                # try the next direction
                continue
            else:
                # copies the array using the python slicing operator ':'
                new_state = [column[:] for column in self.state]
                swap_cells(new_state, empty_tile, (x, y))
                child_node = Node(new_state, self.depth + 1, self)
                children.append(child_node)
        return children


