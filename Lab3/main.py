class KnightsTour:

    POSSIBLE_MOVES = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

    def __init__(self, starting_row, starting_col):
        self._current_step = 1
        self._board = []
        for row in range(8):
            self._board.append([])
            for column in range(8):
                self._board[row].append(' ')
        self.solve(starting_row, starting_col)

    def __str__(self):
        return "\n".join(str(row) for row in self._board) + "\n" + "Solution Number: " + str(self._number_of_solutions)

    def is_solved(self):
        return self._current_step == 64

    def can_move_to(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8 and self._board[row][col] == ' '

    def solve(self, row, col):
        if self.is_solved():
            print(self)
        else:
            self._board[row][col] = self._current_step
            next_moves = []
            for move in KnightsTour.POSSIBLE_MOVES:
                if self.can_move_to(row+move[0], col+move[1]):
                    next_moves.append(Position(self, row+move[0], col+move[1] ))
            next_moves.sort()
            for move in next_moves:
                self._current_step += 1
                self.solve(move.row, move.col)
                if not self.is_solved():
                    self._current_step -= 1
                    self._board[row][col] = ' '



class Position:

    def __init__(self, knights_tour, row, col):
        self.knights_tour = knights_tour
        self.row = row
        self.col = col

    def valid_moves(self):
        moves = 0

        for move in KnightsTour.POSSIBLE_MOVES:
            if self.knights_tour.can_move_to(self.row+move[0], self.col+move[1]):
                moves += 1

    def __lt__(self, other):
        return self.valid_moves() < other.valid_moves()

    def __gt__(self, other):
        return self.valid_moves() > other.valid_moves()

    def __eq__(self, other):
        return self.valid_moves() == other.valid_moves()

tour = KnightsTour(0,0)
