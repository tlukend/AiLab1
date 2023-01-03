import random


def create_random_grid():
    """
    This function creates a random 3 x 3 grid and fills it with random numbers between 0 and 8
    :param: no input
    :return: returns an array in the format [[4, 0, 8],[2, 1, 7],[3, 6, 5]]
    """
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

    # creates new grids as long as the created grid is not solvebale
    while check_solvability(array):
        array = create_random_grid()

    return array


def print_grid(array):
    """
    This function prints a grid
    :param: array: array in the format [[4, 0, 8],[2, 1, 7],[3, 6, 5]]
    :return: print()
    """
    # Christina changed to first for x und seccond for y -> if we change it back also change main grid_goal and check_solvability
    for x in range(0, 3):
        for y in range(0, 3):
            print(str(array[x][y]) + " ", end="")
        print()


def check_solvability(array):
    """
    This function checks the solvability of a created grid and is used in the create_random_grid() function
    :param array: array in the format [[4, 0, 8],[2, 1, 7],[3, 6, 5]]
    :return: Boolean: Puzzle is NOT solvable it returns True to stay in the loop in create_random_grid() and create a
    new grid; If the puzzle is solvable the functions returns False and in create_random_grid() it leaves the loop
    """

    # reference: https://www.youtube.com/watch?v=bhmCmbj9VAg and https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    # 9! possible initial states but only half of these are solvable -> (9!)/2 initial states are solvable)
    # check solvability with inversion count - even: solvable; odd: not solvable
    # It is not possible to solve an instance of 8 puzzle if number of inversions is odd in the input state.
    # In the goal state, there are 0 inversions. So we can reach goal state only from a state which has even inversion count.

    inversion_count = 0
    # converted the 2 dimension array into 1 dimension array because it's easier for doing the inversion count
    array_one_dimension = []
    for x in range(0, 3):
        for y in range(0, 3):
            array_one_dimension.append(array[x][y])

    for i in range(0, len(array_one_dimension)):
        # don't check zero
        if array_one_dimension[i] != 0:
            for k in range(i + 1, len(array_one_dimension)):
                # don't count zero
                if (array_one_dimension[k] != 0) and (array_one_dimension[i] > array_one_dimension[k]):
                    inversion_count += 1
    # check if odd or even
    if (inversion_count % 2) == 0:
        # print('Puzzle is solvable')
        # print('Inversion Count: ' + str(inversion_count))
        # return false to stop the while loop in create_random_grid()
        return False
    else:
        # print('Puzzle is NOT solvable: ' + str(print_grid(array)))
        # print('Inversion Count: ' + str(inversion_count))
        return True


def swap_cells(grid, cell1, cell2):
    """
    This function swaps two numbers in the grid
    :param grid: The actual grid where the swapping takes place
    :param cell1: one number (new_state)
    :param cell2: empty tile
    :return: the 2 cells in grid are swapped
    """
    temp = grid[cell1[0]][cell1[1]]
    grid[cell1[0]][cell1[1]] = grid[cell2[0]][cell2[1]]
    grid[cell2[0]][cell2[1]] = temp
