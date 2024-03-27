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
    
    turns = 0 #Starts at 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] != EMPTY):
                turns=turns+1 #How many non empty spaces = How many turns were played
    if (turns%2):
        return O # if there were odd number of turns is the second player's turn
    else:
        return X # if there were even number of turns is the first player's turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                actions.add((i,j)) #Add to set all empty spaces
    if actions:
        return actions #Return the set if there are any available moves
    else:
        return EMPTY #Return empty if board is full



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Action Invalid, box already ocupied")
    if (action[0] < 0 or action[0] > 3 or action[1] < 0 or action[0] >3):
        raise Exception("Action Invalid, out of bounds")
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3): #Check row for a winner
        if board[row][0] != EMPTY and (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            return board[row][0]

    for col in range(3): #Check col for a winner
        if board[0][col] != EMPTY and (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            return board[0][col]

    if board[0][0] != EMPTY and (board[0][0] == board[1][1] and board[1][1] == board[2][2]): #Check first diagonal
        return board[0][0]
    if board[0][2] != EMPTY and (board[0][2] == board[1][1] and board[1][1] == board[2][0]): #Check second diagonal
        return board[0][2]

    return EMPTY 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == EMPTY and actions(board) == EMPTY: #Se não existe vencedor mas não há mais jogadas possiveis
        return True
    if winner(board) != EMPTY: #Se existe um vencedor
        return True
    else:
        return False
        

def utility(board): #Só é chamada após confirmar que o jogo terminou
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X: #Se o vencedor é X
        return 1
    if winner(board) == O: #Se o vencedor O
        return -1
    else:
        return 0 #Se é um empate


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return EMPTY #If game is over, returns Empty

    turn = player(board) #checks who is playing currently
    bestMove = EMPTY

    if turn == X: #Maximizing player
        maxScore = -math.inf
        for action in actions(board):#Calculates score of every possible move
            score = min_value(result(board,action)) #min_value because next player is the minimizing player
            if score > maxScore:
                maxScore = score #Highest possible score, means best move for the maximizing player
                bestMove = action
        return bestMove
    else: #Minimizing player
        minScore = math.inf
        for action in actions(board):#Calculates score of every possible move
            score = max_value(result(board,action)) #max_value because next player is the maximizing player
            if score < minScore:
                minScore = score #Lowest possible score, means best move for the minimizing player
                bestMove = action
        return bestMove 



def min_value(board):
    if terminal(board): 
        return utility(board) #End of the game, returns the score based on the state 
    score = math.inf # Max Positive
    for action in actions(board):
        score = min(score, max_value(result(board,action))) # Keeps going recursively, "max_value" because next is the maximizing player
    return score

def max_value(board):
    if terminal(board):
        return utility(board) #End of the game, returns the score based on the state
    score = -math.inf # Max Negative
    for action in actions(board):
        score = max(score,min_value(result(board,action))) # Keeps going recursively, "min_value" because next is the minimizing player
    return score 

