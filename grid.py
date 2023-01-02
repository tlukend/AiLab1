# inherits to start and goal (2 extra classes??? - wie wird dies in python gelöst?)
import random


# variables: int i; array[3][3] ... kann sein dass für Befüllung noch ein array[9] benötigt wirdfun

# functions: fill(array); print(array)

# for i in range (0, 8):
#    while (self.is_solved == true):


def create_random_grid():
    array = [[], [], []]
    # a set numbers we are choosing from
    numbers = list(range(0, 9))
    # iterate trough grid and pick random number from numbers, with remove it is guaranteed that the same number will
    # not occur
    for x in range(0, 3):
        for y in range(0, 3):
            number = random.choice(numbers)
            numbers.remove(number)
            array[x].append(number)

    while check_solvability(array):
        array = create_random_grid()

    print('out of while loop')

    return array


def print_grid(array):
    #Christina changed to first for x und seccond for y -> if we change it back also change main grid_goal and check_solvability
    for x in range(0, 3):
        for y in range(0, 3):
            print(str(array[x][y]) + " ", end="")
        print()


def check_solvability(array):
    # reference: https://www.youtube.com/watch?v=bhmCmbj9VAg and https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    # 9! possible initial states but only half of these are solvable -> (9!)/2 initial states are solvable)
    # check solvability with inversion count - even: solvable; odd: not solvable



# grid = create_random_grid()
# print_grid(grid)
# print(grid)
