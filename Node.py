#class Node:

#    def __init__(self, gValue, hValue):
        #f(n) = g(n) + h(n) manhattan oder hamming


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

#def hamming (self, start, goal):
#    temp = 0
#    for i in range (0, 2):
#        for j in range (0,2):
#            if start[i][j] != goal[i][j] and start[i][j]!='_':
#                temp += 1
#    return temp




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
if __name__ == '__main__':
    print('Hello, World!')
#print(node with smallest f(n) && h(n) 00 0)
# also print

