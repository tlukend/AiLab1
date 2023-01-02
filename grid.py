#inherits to start and goal (2 extra classes??? - wie wird dies in python gelöst?)
import random

#variables: int i; array[3][3] ... kann sein dass für Befüllung noch ein array[9] benötigt wirdfun

#functions: fill(array); print(array)

#for i in range (0, 8):
#    while (self.is_solved == true):


def create_random_grid():
    array = [[], [], []]
# a set numbers we are choosing from
    numbers = list(range(0, 9))
#iterate trough grid and pick random number from numbers, with remove it is guaranteed that the same number will
#not occur
    for x in range(0, 3):
        for y in range(0, 3):
            number = random.choice(numbers)
            numbers.remove(number)
            array[x].append(number)
    return array


def print_grid(array):
    for y in range(0, 3):
        for x in range(0, 3):
            print(str(array[x][y]) + " ", end="")
        print()


#grid = create_random_grid()
#print_grid(grid)
#print(grid)