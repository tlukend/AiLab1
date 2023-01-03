import constants
import grid
from grid import swap_cells


class Node:
    #The constructor accepts a 2 dimensional array in which the state of the grid is saved
    #If no parent is passed, parent is set to none
    def __init__(self, state, depth, parent=None):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.heuristic = 0

    # calculates the total costs for a node
    # f(n) = g(n) + h(n), f(n) = total_cost, g(n) = depth, h(n) = heuristic.calculate()
    def total_costs(self):
        return int(self.depth) + int(self.heuristic)

    # returns a hash table - Access time for datatype set is O(1)
    def __hash__(self):
        return hash(str(self.state))

    # compares two objects/states by there values
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.state == other.state

    # to check if children are inside grid
    @staticmethod
    def is_inside_grid(x, y):
        return 0 <= x <= 2 and 0 <= y <= 2

    # to get the number of a position -> returns value only if x and y are really in the grid 3 x 3
    def get_number_at(self, x, y):
        if not self.is_inside_grid(x, y):
            return None
        else:
            return self.state[x][y]

    # returns the coordinates of the empty tile
    def get_empty_tile(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.state[x][y] == 0:
                    return x, y

    def generate_child_states(self):
        children = []
        # coordinates of the empty tiles
        empty_tile = self.get_empty_tile()
        # child states are generated - for each direction
        for direction in constants.DIRECTIONS:
            # vector addition to get the new grid which we can move
            x = empty_tile[0]+direction[0]
            y = empty_tile[1]+direction[1]
            if not self.is_inside_grid(x, y):
                #try the next direction
                continue
            else:
                # copies the array using the python slicing operator ':'
                new_state = [column[:] for column in self.state]
                swap_cells(new_state, empty_tile, (x, y))
                child_node = Node(new_state, self.depth + 1, self)
                children.append(child_node)
        return children

 #   def createChild(self):
        #g(n) = g(n) + 1

#def solve_manhattan (start):
    #current = smallest f(n)
    # create children nodes (raise g(n)+1 and add h(n) of this very child-node)
    # my thinking right now: easier to have a list full of all f(n)'s and
    # in every round sort them and pick the smallest
    # this would - in my eyes - make the most sense and always make sure we choose the lowest cost
    # pick smallest
    # if h(n) == 0 we are done, otherwise to recursive function -> repeat
    # if solved, return goal array

#def solve_hamming (start):
    #current = smallest f(n)
    #create children nodes (raise g(n)+1 and add h(n) of this very child-node)
    # my thinking right now: easier to have a list full of all f(n)'s and
    # in every round sort them and pick the smallest
    # this would - in my eyes - make the most sense and always make sure we choose the lowest cost
    # pick smallest
    # if h(n) == 0 we are done, otherwise to recursive function -> repeat
    # if solved, return goal array


#consider, that there must be a state of not going back
#should we empty the queue after we have chosen a child node?
# if h == 0 , we are done
# do we want to print every state until we reach goal? i say yes


#def init ():
    # initialize array
    # checkIfSolvable
    #f = g + h
    #node


# Press the green button in the gutter to run the script.

#print(node with smallest f(n) && h(n) 00 0)
# also print

