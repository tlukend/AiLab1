# main is our compare?
# import numpy as np
import grid

def main():
    grid_goal = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    grid_list = []
    print(grid.print_grid(grid_goal))
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

