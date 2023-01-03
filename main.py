import grid
from Solver import Solver
from HeuristicHamming import HeuristicHamming
from HeuristicManhattan import HeuristicManhattan
from timeit import default_timer as timer

from Puzzle import Puzzle
from SolverAstar import SolverAstar


def main():
    grid_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    print('Goal State: ')
    grid.print_grid(grid_goal)
    print('\n')

    grid_list = []

    # creates a list of 100 random grids
    for i in range(100):
        grid_list.append(grid.create_random_grid())


    print(str(len(grid_list)) + ' grids are created: \n')
    # k = 1
    for i in grid_list:
        # print("Grid number " + str(k) + ":")
        grid.print_grid(i)
        print()
        # k += 1

    puzzle = Puzzle(grid_goal, grid_goal)
    # solve the 100 puzzles with Hamming
    solverHamming = SolverAstar(HeuristicHamming())
    startHamming = timer()
    for i in grid_list:
        puzzle.start_state = i
        a = solverHamming.solve(puzzle)
        print(a)
    endHamming = timer()
    # also returns or get_len_nodes(because it's a class???) count of all nodes used (memory usage) and
    # deletes all nodes (in class SolverAstar)

    # solve the 100 puzzles with Manhattan
    solverManhatten = SolverAstar(HeuristicManhattan())
    startManhattan = timer()
    for i in grid_list:
        puzzle.start_state = i
        a = solverManhatten.solve(puzzle)
        print(a)
    endManhattan = timer()
    # also returns or get_len_nodes(because it's a class???) count of all nodes used (memory usage) and
    # deletes all nodes (in class SolverAstar)

    # TODO: Memory Usage (number of expanded nodes in the search tree)
    # Measure memory effort (number of nodes expanded) and run time for each of 100 random states and each heuristics

    # TODO: Computation Time
    # reference https://www.programiz.com/python-programming/examples/elapsed-time
    # timeit provides the most accurate results.
    print('Hamming took for ' + str(len(grid_list)) + ' Puzzles : ' + str(endHamming - startHamming) + ' seconds')

    print('Manhattan took for ' + str(len(grid_list)) + ' Puzzles : ' + str(endManhattan - startManhattan) + ' seconds')

    # TODO: Provide mean and standard deviation of memory usage and execution time for each heuristics


if __name__ == "__main__":
    main()



#puzzle = new puzzle()
#solver = new solverAstar(heuristichamming)
#solver.solve(puzzle)

