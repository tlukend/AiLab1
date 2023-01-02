import constants


class Node:
    #The constructor accepts a 2 dimensional array in which the state of the grid is saved
    #If no parent is passed, parent is set to none
    def __init__(self, state, total_cost, parent=None):
        self.state = state
        self.total_cost = total_cost
        self.parent = parent

    @staticmethod
    def is_inside_grid(x, y):
        return x < 0 or x > 2 or y < 0 or y > 2

    def get_number_at(self, x, y):
        if not self.is_inside_grid(x, y):
            return None
        else:
            return self.state[x][y]

    def get_empty_tile(self):
        for x in range(0, 2):
            for y in range(0, 2):
                if self.state[x][y] == 0:
                    return x, y

    def swap_tiles(self, tile1, tile2):
        temp = self.state[tile1[0]][tile1[1]]
        self.state[tile1[0]][tile1[1]] = self.state[tile2[0]][tile2[1]]
        self.state[tile2[0]][tile2[1]] = temp

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
                child_node = Node(self.state.copy(), self.total_cost, self)
                child_node.swap_tiles(empty_tile, (x, y))
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

