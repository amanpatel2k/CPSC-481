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


# Helpler function to check who wins
def winnercheck(board, player):
    
    for row in range(len(board)):

        # Check to all the columns to see if they form 3 O's or 3 X's in consecutive order
        if board[0][row] == player and board[1][row] == player and board[2][row] == player:
            return player 
        
        # Check to all the rows to see if they form 3 O's or 3 X's in consecutive order
        elif board[row][0] == player and board[row][1] == player and board[row][2] == player: 
            return player

    # Check all the Diagonals to see if they form 3 O's or 3 X's in consecutive order
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return player
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player: 
        return player

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Use the helper function to check to see if X or O won
    x_won = winnercheck(board, X) 
    o_won = winnercheck(board, O)

    # Check if X won then return X
    if x_won == X: 
        return X
    # Check if O won then return O
    elif o_won == O:
        return O
    # If X and O did not win then return None 
    else: 
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Grab the winner of the given board
    win = winner(board)

    # If the winner is X or O
    if win == X or win == O:
        # Return True 
        return True 

    # Check to see if there is a TIE game 
    for row in board:
        # If EMPTY exists in the board then return False 
        if EMPTY in row: 
            return False

    # Return True if there is a TIE game 
    return True 


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)

    # Check to see if X won 
    if win == X:
        # If X won then return 1
        return 1
    # Check to see if O won 
    elif win == O:
        # If O won then return -1
        return -1
    # Check to see if it is tie game
    else:
        # If no winner then return 0
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        
        # Grab all possible actions from board 
        possible_actions = actions(board)

        # Keep track of the best action
        best_action = ()

        # If terminal board then return the score and best action
        if terminal(board) == True:
            return score(board), best_action

        # Set max value to negative infinity
        max_value = -math.inf
        # For all action in the possible actions
        for action in possible_actions: 
            # Grab the maximum value from either min_value function or from the max_value
            current_value = max(max_value, min_value((result(board, action)))[0])
            # If current value is greater then max_value 
            if current_value > max_value: 
                # Update the max value and the best action
                max_value = current_value
                best_action = action

        # Return the max value and best action
        return max_value, best_action

    def min_value(board):
 
        # Grab all possible actions from board 
        possible_actions = actions(board)
        
        # Keep track of the best action
        best_action = ()

        # If terminal board then return the score and best action
        if terminal(board) == True:
            return score(board), best_action

        # Set min value to positive infinity
        min_value = math.inf

        # For all action in the possible actions
        for action in possible_actions: 
            # Grab the minimum value from either max_value function or from the min_value
            current_value = min(min_value, max_value((result(board, action)))[0])
            # If current value is less then min_value 
            if current_value < min_value: 
                # Update the min value and the best action
                min_value = current_value
                best_action = action
        
        # Return the max value and best action
        return min_value, best_action


    # Grab the current player from the board
    currentplayer = player(board)

    # If board is a terminal board then return None
    if terminal(board) == None: 
        return None 

    # If current player is X then call the max value function
    if currentplayer == X: 
        # Return the best action from the max value function
        return max_value(board)[1]
    # Else call the min value function
    else:
        # Return the best action from the min value function
        return min_value(board)[1]

