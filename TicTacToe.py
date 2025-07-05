import math

# TIC TAC TOE AI
def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


def check_win(board, player):
    win_states = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_states


def board_full(board):
    return ' ' not in board


def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -1
    elif check_win(board, 'O'):
        return 1
    elif board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def make_move(board):
    best_move = -1
    best_score = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def play_game():
    board = [' '] * 9
    print("Welcome to Tic Tac Toe Ai!")
    print_board(board)
    
    while True:
        # Your turn
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] == ' ':
            board[player_move] = 'X'
            print_board(board)
            
            if check_win(board, 'X'):
                print("Congratulations! You win!")
                break
            elif board_full(board):
                print("It's a draw!")
                break
            
            # AI's turn
            make_move(board)
            print("AI has made its move:")
            print_board(board)
            
            if check_win(board, 'O'):
                print("AI wins!")
                break
            elif board_full(board):
                print("It's a draw!")
                break
        else:
            print("That position is already taken. Please choose an empty spot.")
# Lets play the game.
play_game()