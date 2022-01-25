class SudokoSolver:

    def __init__(self, board):
        self.board = board
        self.row_index = 0
        self.column_index = 0

    def __str__(self):
        # result = ""
        # for row in self.board:
        #    result += str(row) + "\n"
        # return result

        return "\n".join(str(row) for row in self.board)

    def solve(self):
        print(self)
        print(self.row_index, self.column_index)
        if self.row_index > 8:
            print(self)

        if self._is_unsolved():
            # FIXME this, if the space is taken, advance row/col
            if self.board[self.row_index][self.column_index] == " ":
                for number in range(1, 10):
                    number = str(number)
                    if self._can_place(number, self.row_index, self.column_index):
                        self.board[self.row_index][self.column_index] = number
                        self.column_index += 1
                        if self.column_index > 8:
                            self.column_index = 0
                            self.row_index += 1
                        self.solve()
                        if self._is_unsolved():  # undo because it was a dead end
                            self.column_index -= 1
                            if self.column_index < 0:
                                self.column_index = 8
                                self.row_index -= 1
                            self.board[self.row_index][self.column_index] = " "

    def _can_place_in_row(self, number, row_index):
        return number not in self.board[row_index]

    def _can_place_in_column(self, number, column_index):
        for row in self.board:
            if number == row[column_index]:
                return False
        return True

    def _can_place_in_3by3(self, number, row_index, column_index):
        starting_row = row_index // 3 * 3
        starting_column = column_index // 3 * 3

        for row_index in range(starting_row, starting_row + 3):
            for column_index in range(starting_column, starting_column + 3):
                if self.board[row_index][column_index] == number:
                    return False

        return True

    def _can_place(self, number, row_index, column_index):
        return self._can_place_in_row(number, row_index) and \
               self._can_place_in_column(number, column_index) and \
               self._can_place_in_3by3(number, row_index, column_index)

    def _is_unsolved(self):
        for row in self.board:
            if " " in row:
                return True
        return False


board = [
    [" ", " ", "5", " ", " ", "8", " ", "4", " "],
    ["4", "1", "7", " ", " ", "6", " ", " ", " "],
    [" ", "8", " ", " ", "5", "9", "1", "7", " "],
    ["7", " ", " ", "1", " ", " ", "8", "3", " "],
    [" ", " ", " ", "9", "7", "3", " ", " ", " "],
    [" ", "9", "3", " ", " ", "4", " ", " ", "6"],
    [" ", " ", " ", " ", " ", " ", " ", "9", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "]
]
solver = SudokoSolver(board)

solver.solve()
print(solver)
