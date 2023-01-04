import grid
from HeuristicHamming import HeuristicHamming
from HeuristicManhattan import HeuristicManhattan
from timeit import default_timer as timer
from statistics import mean

from Puzzle import Puzzle
from SolverAstar import SolverAstar


def main():
    """
    In the main the static goal_grid is created,
    the memory effort and execution time of each heuristic is calculated,
    100 grids are created and solved using Hamming and Manhattan
    and finally it prints all these information
    :return: nothing
    """
    grid_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    print('\n################\n#   8-PUZZLE   #'
          '\n################\n')
    print('Goal State: ')
    grid.print_grid(grid_goal)

    all_nodes_hamming = 0
    all_nodes_manhattan = 0
    grid_list = []
    runtime_list_hamming = []
    # TODO: Es wird nirgendwo etwas in runtime list manhattan eingefügt?
    runtime_list_manhattan = []

    # creates a list of 100 random grids
    start_creating_grid = timer()
    for i in range(3):
        grid_list.append(grid.create_random_grid())
    end_creating_grid = timer()

    print('\nCreating ' + str(len(grid_list)) + ' puzzles takes ' + str(end_creating_grid - start_creating_grid)
          + ' seconds.\n')

    print('############################################\n# Solving 8-Puzzle using Hamming Heuristic #'
          '\n############################################\n')

    puzzle = Puzzle(grid_goal, grid_goal)
    # solve the 100 puzzles with Hamming
    start_hamming = timer()
    solver_hamming = SolverAstar(HeuristicHamming())
    grid_counter = 1
    for i in grid_list:
        start_single_hamming = timer()
        puzzle.start_state = i
        print('[' + str(grid_counter) + ']' + ' Puzzle start_state: ')
        grid_counter += 1
        grid.print_grid(puzzle.start_state)
        a, len_open_nodes = solver_hamming.solve(puzzle)

        # calculate and save runtime for each puzzle (for mean and standard deviation)
        end_single_hamming = timer()
        # TODO: Falsch? End minus start wäre richtig?
        runtime_list_hamming.append(end_single_hamming - start_single_hamming)

        print('\nThis is the return (current state) if the puzzle is solved:')
        grid.print_grid(a.state)

        # print('Is return (current state) the same as goal_state? ' + str(a.state == grid_goal))
        if a.state != grid_goal:
            print('\n!!!!Puzzle not solved!!!\n')

        # print depth
        print("Depth of the tree to solve this puzzle: " + str(a.depth))

        all_nodes_hamming += len_open_nodes
        print("This puzzle needed " + str(len_open_nodes) + " nodes to be created.\n")

    end_hamming = timer()

    print('#############################################\n# Solving 8-Puzzle using Manhattan Heuristic #'
          '\n#############################################\n')
    # solve the 100 puzzles with Manhattan
    start_manhattan = timer()
    solver_manhattan = SolverAstar(HeuristicManhattan())
    grid_counter = 1
    for i in grid_list:
        start_single_manhattan = timer()
        puzzle.start_state = i
        print('[' + str(grid_counter) + ']' + ' Puzzle start_state: ')
        grid_counter += 1
        grid.print_grid(puzzle.start_state)
        a, len_open_nodes = solver_manhattan.solve(puzzle)

        end_single_manhattan = timer()
        # TODO: Falsch? End minus start wäre richtig?
        runtime_list_manhattan.append(end_single_manhattan - start_single_manhattan)

        print('\nThis is the return (current state) if the puzzle is solved:')
        grid.print_grid(a.state)

        # print('Is return (current state) the same as goal_state? ' + str(a.state == grid_goal))
        if a.state != grid_goal:
            print('\n!!!!Puzzle not solved!!!\n')

        # print depth
        print("Depth of the tree to solve the puzzle: " + str(a.depth))

        all_nodes_manhattan += len_open_nodes
        print("This puzzle needed " + str(len_open_nodes) + " nodes to be created.\n")

    end_manhattan = timer()

    # also returns or get_len_nodes(because it's a class???) count of all nodes used (memory usage) and
    # deletes all nodes (in class SolverAstar)

    # TODO: Memory Usage (number of expanded nodes in the search tree)
    # TODO: es sind jetzt folgende nodes enthalten: start_node, open_nodes, open_nodes_set, closed_nodes_set,
    #  child_node, children
    # Measure memory effort (number of nodes expanded) and run time for each of 100 random states and each heuristics
    print("\n################\n# Memory Usage #\n################\n")
    print("The following nodes are counted: start_node, open_nodes, open_nodes_set, closed_nodes_set, "
          "child_node, children; \n")
    print("Hamming needs for " + str(len(grid_list)) + " puzzles " + str(all_nodes_hamming)
          + " nodes to be created.")

    print("Manhattan needs for " + str(len(grid_list)) + " puzzles " + str(all_nodes_manhattan)
          + " nodes to be created.")

    # TODO: Computation Time
    # reference https://www.programiz.com/python-programming/examples/elapsed-time
    # timeit provides the most accurate results.
    print('\n####################\n# Computation Time #\n####################\n')
    print('Hamming took for ' + str(len(grid_list)) + ' Puzzles ' + str(end_hamming - start_hamming) + ' seconds.')

    print(
        'Manhattan took for ' + str(len(grid_list)) + ' Puzzles ' + str(end_manhattan - start_manhattan) + ' seconds.')

    # TODO: Provide mean and standard deviation of memory usage and execution time for each heuristics

    # calculation and printing of mean time for hamming
    mean_hamming = mean(runtime_list_hamming)
    print('\n###############################\n# Mean and standard deviation #\n###############################\n')
    print('Mean time to solve Hamming is ' + str(mean_hamming) + ' seconds.')

    # calculation and printing of mean time for manhattan
    mean_manhattan = mean(runtime_list_manhattan)
    print('Mean time to solve Manhattan is ' + str(mean_manhattan) + ' seconds.')

    # calculation of standard deviation time for hamming
    std_deviation_hamm = []
    for i in runtime_list_hamming:
        std_deviation_hamm.append(abs(i - mean_hamming))

    # calculation of standard deviation time for manhattan
    std_deviation_man = []
    for i in runtime_list_manhattan:
        std_deviation_man.append(abs(i - mean_manhattan))

    # printing of standard deviation times
    print('Standard deviation Hamming: ' + str(std_deviation_hamm))
    print('Standard deviation Manhattan: ' + str(std_deviation_man))


if __name__ == "__main__":
    main()

# puzzle = new puzzle()
# solver = new solverAstar(heuristichamming)
# solver.solve(puzzle)
