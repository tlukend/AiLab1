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
    start_creating_grid = timer()
    for i in range(1):
        grid_list.append(grid.create_random_grid())
    end_creating_grid = timer()

    print('Creating ' + str(len(grid_list)) + ' puzzles takes ' + str(end_creating_grid - start_creating_grid)
          + ' seconds.')

    #print(str(len(grid_list)) + ' grids are created: \n')
    # k = 1
    #for i in grid_list:
        # print("Grid number " + str(k) + ":")
        # grid.print_grid(i)
        # print()
        # k += 1

    puzzle = Puzzle(grid_goal, grid_goal)
    # solve the 100 puzzles with Hamming
    start_hamming = timer()
    solver_hamming = SolverAstar(HeuristicHamming())
    for i in grid_list:
        puzzle.start_state = i
        print('Puzzle start_state: ')
        grid.print_grid(puzzle.start_state)
        a = solver_hamming.solve(puzzle)

        # print nodes
        print('This is the return (current state) if the puzzle is solved: is it like Goal State')
        grid.print_grid(a.state)

        # print depth
        print("depth of the solution which are the steps used to solve the puzzle: " + str(a.depth))

    end_hamming = timer()
    # also returns or get_len_nodes(because it's a class???) count of all nodes used (memory usage) and
    # deletes all nodes (in class SolverAstar)

    # solve the 100 puzzles with Manhattan

    #start_manhattan = timer()
    #solver_manhatten = SolverAstar(HeuristicManhattan())
    #for i in grid_list:
        #puzzle.start_state = i
        #a = solver_manhatten.solve(puzzle)
        #print(a)

        #print('Now start_state == grid_goal if solved: ')
        #grid.print_grid(puzzle.start_state)
    #end_manhattan = timer()

    # also returns or get_len_nodes(because it's a class???) count of all nodes used (memory usage) and
    # deletes all nodes (in class SolverAstar)


    """
    print nodes:
            for i in open_nodes_set:
            print(i.state)
    """

    # TODO: Memory Usage (number of expanded nodes in the search tree)
    # Measure memory effort (number of nodes expanded) and run time for each of 100 random states and each heuristics

    # TODO: Computation Time
    # reference https://www.programiz.com/python-programming/examples/elapsed-time
    # timeit provides the most accurate results.
    print('Hamming took for ' + str(len(grid_list)) + ' Puzzles : ' + str(end_hamming - start_hamming) + ' seconds')

    #print('Manhattan took for ' + str(len(grid_list)) + ' Puzzles : ' + str(end_manhattan - start_manhattan)
     #     + ' seconds')

    # TODO: Provide mean and standard deviation of memory usage and execution time for each heuristics


if __name__ == "__main__":
    main()



#puzzle = new puzzle()
#solver = new solverAstar(heuristichamming)
#solver.solve(puzzle)

