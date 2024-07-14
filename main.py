# This solver can be run by executing `python main.py` in a terminal.
# There is an example input in the main method, line 77. One can replace it for testing.

class TicTacToeSolver:
    def __init__(self, board=None):
        if board:
            # size validation only, could use more validation
            if len(board) == 4 and len(board[0]) == 4:
                self.board = board
            else:
                print("invalid board presentation")
        else:
            self.board = self.create_board()

    def create_board(self):
        return [[self.EMPTY] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]

    def checkWinner(self):
        for rule in TicTacToeSolver.WINNING_RULES:
            for positions in rule:
                values = [self.board[row][col] for row, col in positions]
                if TicTacToeSolver.EMPTY in values:
                    continue
                else:
                    if values.count(values[0]) == 4:
                        return values[0]
        return None

    def anyMovesLeft(self):
        for row in self.board:
            if TicTacToeSolver.EMPTY in row:
                return True
        return False

    def isGameOver(self):
        if self.checkWinner() or not self.anyMovesLeft():
            return True
        return False

    # constant definition starts here
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2
    # more players can be added, e.g. PLAYER_3 = 3
    BOARD_SIZE = 4
    # HORIZONTAL_WINNING_POS should be [[(0,0),(0,1),(0,2),(0,3)],[(1,0),(1,1),(1,2),(1,3)],[(2,0),(2,1),(2,2),(2,3)],[(3,0),(3,1),(3,2),(3,3)]]
    HORIZONTAL_WINNING_POS = [[(i, j) for j in range(4)] for i in range(4)]
    # VERTICAL_WINNING_POS should be [[(0,0),(1,0),(2,0),(3,0)],[(0,1),(1,1),(2,1),(3,1)],[(0,2),(1,2),(2,2),(3,2)],[(0,3),(1,3),(2,3),(3,3)]]
    VERTICAL_WINNING_POS = [[(i, j) for i in range(4)] for j in range(4)]
    DIAGONAL_WINNING_POS = [[(0,0),(1,1),(2,2),(3,3)],[(0,3),(1,2),(2,1),(3,0)]]
    CORNER_WINNING_POS = [[(0,0),(0,3),(3,0),(3,3)]]

    def generate_2x2_boxes():
        boxes = []
        for i in range(3):
            for j in range(3):
                box = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
                boxes.append(box)
        return boxes
    BOX_WINNING_POS = generate_2x2_boxes()
    # BOX_WINNING_POS = [
    # [(0, 0), (0, 1), (1, 0), (1, 1)],
    # [(0, 1), (0, 2), (1, 1), (1, 2)],
    # [(0, 2), (0, 3), (1, 2), (1, 3)],
    # [(1, 0), (1, 1), (2, 0), (2, 1)],
    # [(1, 1), (1, 2), (2, 1), (2, 2)],
    # [(1, 2), (1, 3), (2, 2), (2, 3)],
    # [(2, 0), (2, 1), (3, 0), (3, 1)],
    # [(2, 1), (2, 2), (3, 1), (3, 2)],
    # [(2, 2), (2, 3), (3, 2), (3, 3)]
    # ]

    WINNING_RULES = [HORIZONTAL_WINNING_POS, VERTICAL_WINNING_POS, DIAGONAL_WINNING_POS, CORNER_WINNING_POS, BOX_WINNING_POS]

if __name__ == '__main__':
    # example board input
    board = [[1, 2, 0, 2],  [1, 2, 0, 1], [2, 2, 1, 2], [2, 2, 1, 2]]
    tttSolver = TicTacToeSolver(board)
    print("winner:" + str(tttSolver.checkWinner()))
    print("anyMovesLeft:" + str(tttSolver.anyMovesLeft()))
    print("isGameOver:" + str(tttSolver.isGameOver()))