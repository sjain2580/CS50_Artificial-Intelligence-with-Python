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
    if terminal(board):
        return None  # No turn if game is over
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O  # X starts, then alternate


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return set()  # No actions if game is over
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board) or not (0 <= action[0] <= 2 and 0 <= action[1] <= 2) or board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action")
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for combo in [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # Rows
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # Columns
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]  # Diagonals
    ]:
        if all(board[i][j] == X for i, j in combo):
            return X
        if all(board[i][j] == O for i, j in combo):
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        raise ValueError("Utility called on non-terminal board")
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Ensures a draw against optimal play, win if human errs.
    """
    if terminal(board):
        return None

    best_score = float('inf') if player(board) == O else float('-inf')  # Invert for AI's perspective
    best_action = None

    for action in actions(board):
        new_board = result(board, action)
        score = minimax_helper(new_board, player(board) == O)  # Pass maximizing flag
        print(f"Action: {action}, Score: {score}")
        if player(board) == O:
            if score < best_score:  # Minimize score for AI (prefer -1 or 0 over 1)
                best_score = score
                best_action = action
        else:
            if score > best_score:  # Maximize score for human
                best_score = score
                best_action = action

    return best_action


def minimax_helper(board, is_maximizing):
    """
    Helper function to compute the minimax score recursively.
    Returns the utility score for terminal states.
    """
    if terminal(board):
        return utility(board)

    best_score = float('-inf') if is_maximizing else float('inf')

    for action in actions(board):
        new_board = result(board, action)
        score = minimax_helper(new_board, not is_maximizing)  # Alternate maximizing/minimizing
        if is_maximizing:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score