class MazeSolver:

    def __init__(self, maze):
        self._maze = maze
        self._current_steps = 0
        self._steps_per_solution = {}
        for row_index in range(len(maze)):
            for column_index in range(len(self._maze[row_index])):
                if self._maze[row_index][column_index] == 'S':
                    self.solve(row_index, column_index)

    def shortest_path(self):
        try:
            return self._steps_per_solution[min(self._steps_per_solution.keys())]
        except ValueError as e:
            return "No solutions found"

    def solve(self, row_index, column_index):

        # base case - solved
        if self._maze[row_index][column_index] == 'E':
            #print(self)
            self._steps_per_solution[self._current_steps] = str(self)
            return

        # marking that we stepped somewhere, except on S
        if self._maze[row_index][column_index] != 'S':
            self._maze[row_index][column_index] = 'x'

        self._current_steps += 1

        # up
        self._try_move(row_index - 1, column_index)

        # down
        self._try_move(row_index + 1, column_index)

        # left
        self._try_move(row_index, column_index - 1)

        # right
        self._try_move(row_index, column_index + 1)

        # base case, reached a dead end from the recursion
        if self._maze[row_index][column_index] != 'S':
            self._maze[row_index][column_index] = ' '
        self._current_steps -= 1

    def _try_move(self, row_index, column_index):
        if self._can_move_to(row_index, column_index):
            self.solve(row_index, column_index)

    def _can_move_to(self, row_index, column_index):
        return 0 <= row_index < len(self._maze) and 0 <= column_index < len(self._maze[row_index]) and \
            (self._maze[row_index][column_index] == ' ' or self._maze[row_index][column_index] == 'E')

    # https://github.com/EricCharnesky/CIS2001-Winter2021/blob/main/NQueens/NQueens.py#L64
    def __str__(self):
        result = ""
        for row in self._maze:
            result += str(row) + '\n'
        result += f'{self._current_steps} steps\n'
        return result


if __name__ == '__main__':
    maze = [
        ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
        ['W', 'W', ' ', 'W', ' ', ' ', 'W', 'W', 'W', ' '],
        [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' '],
        [' ', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' '],
        [' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' '],
        [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E']
    ]

    solver = MazeSolver(maze)
    print(solver.shortest_path())

    #for solution in solver._steps_per_solution.values():
    #    print(solution)
