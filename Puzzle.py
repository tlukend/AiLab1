"""Puzzle class: knows two states. The randomly generated start_state and the designated grid_goal state """


class Puzzle:
    def __init__(self, start_state, grid_goal):
        self.start_state = start_state
        self.grid_goal = grid_goal
