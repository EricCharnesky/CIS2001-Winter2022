class NQueens:

    def __init__(self, number_of_queens=8):
        self._total_queens = number_of_queens
        self._current_number_of_queens = 0
        self._board = []
        for row in range(number_of_queens):
            self._board.append([])
            for column in range(number_of_queens):
                self._board[row].append(' ')

        self.solve()

    def __str__(self):
        return "\n".join(str(row) for row in self._board)

    def is_solved(self):
        return self._current_number_of_queens == self._total_queens

    def solve(self):
        if self.is_solved():
            print(self)
        else:
            for row_index in range(self._total_queens):
                if not self.is_solved() and self._can_place_queen(row_index):
                    self._board[row_index][self._current_number_of_queens] = 'Q'
                    self._current_number_of_queens += 1
                    self.solve()
                    if not self.is_solved():
                        self._current_number_of_queens -= 1
                        self._board[row_index][self._current_number_of_queens] = ' '

    def _is_row_open(self, row_index):
        return 'Q' not in self._board[row_index]

    def _is_upward_diagonal_open(self, row_index):
        current_column_index = self._current_number_of_queens - 1
        current_row_index = row_index - 1

        while current_row_index >= 0 and current_column_index >= 0:
            if self._board[current_row_index][current_column_index] == 'Q':
                return False
            current_row_index -= 1
            current_column_index -= 1

        return True

    def _is_downward_diagonal_open(self, row_index):
        current_column_index = self._current_number_of_queens - 1
        current_row_index = row_index + 1

        while current_row_index < self._total_queens and current_column_index >= 0:
            if self._board[current_row_index][current_column_index] == 'Q':
                return False
            current_row_index += 1
            current_column_index -= 1

        return True


    def _can_place_queen(self, row_index):
        return self._is_row_open(row_index) and \
        self._is_upward_diagonal_open(row_index) and \
        self._is_downward_diagonal_open(row_index)



eightQueens = NQueens()


