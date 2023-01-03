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

    def total_costs(self):
        return self.depth + self.heuristic

    def __hash__(self):
        return hash(str(self.state))

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.state == other.state

    @staticmethod
    def is_inside_grid(x, y):
        return 0 <= x <= 2 and 0 <= y <= 2

    def get_number_at(self, x, y):
        if not self.is_inside_grid(x, y):
            return None
        else:
            return self.state[x][y]

    def get_empty_tile(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.state[x][y] == 0:
                    return x, y

    def generate_child_states(self):
        children = []
        #koordinaten von leeren Kästchen
        empty_tile = self.get_empty_tile()
        # childstates werden generiert
        for direction in constants.DIRECTIONS:
            #Vektoraddition um auf das neue Kästchen zu kommen das wir verschieben können
            x = empty_tile[0]+direction[0]
            y = empty_tile[1]+direction[1]
            if not self.is_inside_grid(x, y):
                continue
            else:
                new_state = self.state.copy();
                new_state[0] = new_state[0].copy();
                new_state[1] = new_state[1].copy();
                new_state[2] = new_state[2].copy();
                swap_cells(new_state, empty_tile, (x, y))
                child_node = Node(new_state, self.depth + 1, self)
                children.append(child_node)
        return children


    #da kommt noch mehr logik rein



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

