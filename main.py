# main is our compare?
# import numpy as np
import grid

def main():
    grid_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    grid_list = []

    #list 100 arrays
    for i in range(100):
        grid_list.append(grid.create_random_grid())

    #prints length and arrays
    print(str(len(grid_list)) + ' grids are created: \n')
    for i in grid_list:
        grid.print_grid(i)
        print()



if __name__ == "__main__":
    main()



#puzzle = new puzzle()
#solver = new solverAstar(heuristichamming)
#solver.solve(puzzle)

