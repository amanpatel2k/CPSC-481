"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

# Raise Exception Class to display if an action is not valid
class NotValidActionError(Exception): 
    def __init__(self, action):
        self.action = action
        self.message = f"This action, {self.action}, is not valid"
        super().__init__(self.message)

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
    # If board is initial state
    if board == initial_state():
        # Let X start
        return X
    
    # Else if board is terminal
    elif board == terminal(board):
        # Return Any Value 
        return None
    
    # Else
    else:
        o_counter = 0
        x_counter = 0
        # Trace through the entire board 
        for row in board:
            for col in row: 
             # Count the # of X and O
                if col == X: 
                    x_counter += 1
                elif col == O:
                    o_counter += 1
            
        # If # of X > # of O
        if x_counter > o_counter: 
            # Return O
            return O
        # Else:
        else:
            # X Turn
            return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create a set to store all the possible available action
    possible_actions = []
    # For each (i, j) in board: 
    for row in range(len(board)):
        for col in range(len(board[row])): 
             # If (i, j) == EMPTY:
            if board[row][col] == EMPTY:
                # Append to the (i, j) to a set 
                possible_actions.append((row,col))

    # Return all possible available action            
    return possible_actions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Keep a deep copy of the board 
    board_clone = copy.deepcopy(board)

    # Grab the current player
    current_player = player(board_clone)

    row, col = action

    # If action is not valid 
    if board_clone[row][col] != EMPTY: 
        raise NotValidActionError(action)

    # Update the board with the action and current player
    else:
        board_clone[row][col] = current_player
    
    return board_clone


    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
