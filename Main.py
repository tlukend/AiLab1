import Grid
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
    100 grids are created and solved using Hamming and Manhattan,
    and finally it prints all these information
    :return: nothing
    """
    grid_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    print('\n################\n#   8-PUZZLE   #'
          '\n################\n')
    print('Goal State: ')
    Grid.print_grid(grid_goal)

    all_nodes_hamming = 0
    all_nodes_manhattan = 0
    grid_list = []
    runtime_list_hamming = []
    runtime_list_manhattan = []

    # creates a list of 100 random grids
    start_creating_grid = timer()
    for i in range(100):
        grid_list.append(Grid.create_random_grid())
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
        puzzle.start_state = i
        print('[' + str(grid_counter) + ']' + ' Puzzle start_state: ')
        grid_counter += 1
        Grid.print_grid(puzzle.start_state)

        start_single_hamming = timer()

        a, len_open_nodes = solver_hamming.solve(puzzle)

        # calculate and save runtime for each puzzle (for mean and standard deviation)
        end_single_hamming = timer()
        runtime_list_hamming.append(end_single_hamming - start_single_hamming)

        print('\nThis is the return (current state) if the puzzle is solved:')
        Grid.print_grid(a.state)

        if a.state != grid_goal:
            print('\n!!!!Puzzle not solved!!!\n')

        # print depth
        print("Depth of the tree to solve this puzzle: " + str(a.depth))

        all_nodes_hamming += len_open_nodes
        print("This puzzle needs to create " + str(len_open_nodes) + " expanded nodes.\n")

    end_hamming = timer()

    print('#############################################\n# Solving 8-Puzzle using Manhattan Heuristic #'
          '\n#############################################\n')
    # solve the 100 puzzles with Manhattan
    start_manhattan = timer()
    solver_manhattan = SolverAstar(HeuristicManhattan())
    grid_counter = 1
    for i in grid_list:
        puzzle.start_state = i
        print('[' + str(grid_counter) + ']' + ' Puzzle start_state: ')
        grid_counter += 1
        Grid.print_grid(puzzle.start_state)

        start_single_manhattan = timer()

        a, len_open_nodes = solver_manhattan.solve(puzzle)

        end_single_manhattan = timer()
        runtime_list_manhattan.append(end_single_manhattan - start_single_manhattan)

        print('\nThis is the return (current state) if the puzzle is solved:')
        Grid.print_grid(a.state)

        if a.state != grid_goal:
            print('\n!!!!Puzzle not solved!!!\n')

        # print depth
        print("Depth of the tree to solve the puzzle: " + str(a.depth))

        all_nodes_manhattan += len_open_nodes
        print("This puzzle needs to create " + str(len_open_nodes) + " expanded nodes.\n")

    end_manhattan = timer()

    # also returns or get_len_nodes(because it's a class???) count of all nodes used (memory usage) and
    # deletes all nodes (in class SolverAstar)

    # Memory Usage (number of expanded nodes in the search tree)
    # contains the following nodes: start_node, open_nodes, open_nodes_set, closed_nodes_set, child_node, children
    # Measure memory effort (number of nodes expanded) and run time for each of 100 random states and each heuristic
    print("\n################\n# Memory Usage #\n################\n")
    print("The following nodes are counted: closed_nodes (expanded nodes) "
          "child_node, children; \n")
    print("Hamming needs for " + str(len(grid_list)) + " puzzles " + str(all_nodes_hamming)
          + " expanded nodes.")

    print("Manhattan needs for " + str(len(grid_list)) + " puzzles " + str(all_nodes_manhattan)
          + " expanded nodes.")

    # Computation Time
    # reference https://www.programiz.com/python-programming/examples/elapsed-time
    # timeit provides the most accurate results.
    print('\n####################\n# Computation Time #\n####################\n')
    print('Hamming took for ' + str(len(grid_list)) + ' Puzzles ' + str(end_hamming - start_hamming) + ' seconds.')

    print(
        'Manhattan took for ' + str(len(grid_list)) + ' Puzzles ' + str(end_manhattan - start_manhattan) + ' seconds.')

    # calculation of total computation time for Hamming plus Manhattan
    total_time = 0.0
    ham_time_count = 0
    man_time_count = 0
    while ham_time_count < len(runtime_list_hamming):
        total_time += runtime_list_hamming[ham_time_count]
        ham_time_count += 1

    while man_time_count < len(runtime_list_manhattan):
        total_time += runtime_list_manhattan[man_time_count]
        man_time_count += 1

    print('\n--------------------------------------------\nTotal computation time : ' + str(total_time) +
          '\n--------------------------------------------\n')

    # Provide mean and standard deviation of memory usage and execution time for each heuristic
    # calculation and printing of mean for Hamming-time
    mean_hamming = mean(runtime_list_hamming)
    print('\n###############################\n# Mean and standard deviation #\n###############################\n')
    print('Mean time to solve Hamming is ' + str(mean_hamming) + ' seconds.')

    # calculation and printing of standard deviation for Hamming-time
    print('\nStandard deviation for Hamming-time:')
    std_deviation_ham = []
    ham_stddev_counter = 0
    for i in runtime_list_hamming:
        std_deviation_ham.append(abs(runtime_list_hamming[ham_stddev_counter] - mean_hamming))
        print('Puzzle ' + str(ham_stddev_counter + 1) + ': ' + str(std_deviation_ham[ham_stddev_counter]))
        ham_stddev_counter += 1

    # printing list of Hamming-times
    ham_runtime_counter = 0
    print('\nRuntime list for Hamming-times:')
    for i in runtime_list_hamming:
        print('Puzzle ' + str(ham_runtime_counter + 1) + ': ' + str(runtime_list_hamming[ham_runtime_counter]))
        ham_runtime_counter += 1

    print('\n-----------------')
    # calculation and printing of mean Manhattan-time
    mean_manhattan = mean(runtime_list_manhattan)
    print('\nMean time to solve Manhattan is ' + str(mean_manhattan) + ' seconds.')

    # calculation and printing of standard deviation for Manhattan-time
    print('\nStandard deviation for Manhattan-time:')
    std_deviation_man = []
    man_stddev_counter = 0
    for i in runtime_list_manhattan:
        std_deviation_man.append(abs(runtime_list_manhattan[man_stddev_counter] - mean_manhattan))
        print(
            'Puzzle ' + str(man_stddev_counter + 1) + ': ' + str(std_deviation_man[man_stddev_counter]))
        man_stddev_counter += 1

    # printing list of Manhattan-times
    man_runtime_counter = 0
    print('\nRuntime list for Manhattan-times:')
    for i in runtime_list_manhattan:
        print('Puzzle ' + str(man_runtime_counter + 1) + ': ' + str(runtime_list_manhattan[man_runtime_counter]))
        man_runtime_counter += 1


if __name__ == "__main__":
    main()
