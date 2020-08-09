"""
Tic Tac Toe Player
"""


import math
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    no_of_empty = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                no_of_empty += 1

    if no_of_empty % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Row Checking
    if board[0][0] == board[0][1] == board[0][2] != EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != EMPTY:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != EMPTY:
        return board[2][0]

    # Column Checking
    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != EMPTY:
        return board[0][2]

    # Diag Checking
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)

    if win == X or win == O:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #if board == initial_state():
    #    return 1, 1

    if terminal(board):
        return None

    mark = player(board)
    max_prune = -math.inf
    min_prune = math.inf
    if mark == X:
        return max_choice(board, max_prune, min_prune)[1]
    else:
        return min_choice(board, max_prune, min_prune)[1]

def max_choice(board, max_prune, min_prune):
    best_move = None

    if terminal(board):
        return [utility(board), best_move]

    curr_best = -math.inf
    for move in actions(board):
        value = min_choice(result(board, move), max_prune, min_prune)[0]
        max_prune = max(max_prune, value)
        if value > curr_best:
            curr_best = value
            best_move = move
        if max_prune >= min_prune:
            break
    return [curr_best, best_move]


def min_choice(board, max_prune, min_prune):
    best_move = None

    if terminal(board):
        return [utility(board), best_move]

    curr_best = math.inf
    for move in actions(board):
        value = max_choice(result(board, move), max_prune, min_prune)[0]
        min_prune = min(min_prune, value)
        if value < curr_best:
            curr_best = value
            best_move = move
        if max_prune >= min_prune:
            break
    return [curr_best, best_move]