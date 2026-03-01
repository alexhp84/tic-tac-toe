#importing the needed modules
import random
import time

#defining the icons
O = "⭕"
X = "❌"

#setting the scores
player1_score = 0
player2_score = 0
draws = 0

#this is creating the logic for the board, assigning each square a reference number between 1 to 9
def create_board():
    return [str(i) for i in range(1, 10)]

#this is printing the board, and showing which square is which number to help the player/s
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("***|***|***")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("***|***|***")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

#this is defining a computer opponent
def computer_move(board):
    #first, this will attempt to win, running the game for winning combinations
    for i in range(9):
        if board[i] not in [X, O]:
            board_copy = board[:]
            board_copy[i] = O
            if check_winner(board_copy, O):
                board[i] = O
                return

    #this will check for the human opponents attempt to win and block
    for i in range(9):
        if board[i] not in [X, O]:
            board_copy = board[:]
            board_copy[i] = X
            if check_winner(board_copy, X):
                board[i] = O
                return

    #this is to move randomly choosing a free square if there is no win or block
    free = [i for i in range(9) if board[i] not in [X, O]]
    if free:א
        board[random.choice(free)] = O
        return

#defines the first players name
name = input("Hi Player 1, please enter your name: ")

#define how to play
def play_mode():
    #defining if playing against a human (1) or AI (2)
    #the definition of a human taken from Star Trek TNG from a robotic life forms name for humans
    choice = input(f"Hi {name}, do you want to play against another bag of mostly water (1) or me (2)? ")

    #defining play order
    if choice == "2":
        order = input(f"Hi {name}, do you want to go first (1) or should I (2)? ")
        if not choice.isdigit():
            order = input(f"Hi {name}, do you want to go first (1) or should I (2)? ")
        return choice, order

    elif choice == "1":
        order = input(f"Hi {name}, do you wish to go first (1) or second(2)?")
        if not choice.isdigit():
            order = input(f"{name} please make a choice to go first (1) or second(2)?")
        return choice, order
    return choice, "1"

#asking the current player for a move and is a valid digit
def player_move(board, current_name, symbol):
    while True:
        choice = input(f"{current_name}, please choose a square (1-9): ")

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice = int(choice)
        if choice < 1 or choice > 9:
            print("Number must be between 1 and 9.")
            continue

        if board[choice - 1] in [X, O]:
            print("That square is already taken.")
            continue

        board[choice - 1] = symbol
        break

#defining the win combinations and pattern match
def check_winner(board, symbol):
    win = ([0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8])
    for pattern in win:
        if all(board[i] == symbol for i in pattern):
            return True
    return False

#function to check if there is a tie, only if the board is full
def is_tie(board):
    if check_winner(board, O) or check_winner(board, X):
        return False
    return all(cell in [X, O] for cell in board)


def switch_player(player1, current_name, player2):
    if current_name == player1:
        return player2
    else:
        return player1

#to ask either player if they want another game
def replay_game():
    choice = input(f"{name} do you wish to play again? Y(es) ir N(o)?")
    if choice in ["Y","y", "Yes", "yes", "YES"]:
        return True
    else:
        return False

#defining how the game if played using the above functions as a function
def play_game():
    # defining the board and the play mode & order
    global player1_score, player2_score, draws
    board = create_board()
    mode, order = play_mode()

    player1 = name
    if mode == "2":
        player2 = "Computer"
    else:
        player2 = input("Hi Player 2, please enter your name: ")

    if order == "1":
        current_icon = X
        current_name = player1
    else:
        current_icon = O
        current_name = player2

    while True:
        print_board(board)

        # computer move
        if mode == "2" and current_name == "Computer":
            time.sleep(1)
            computer_move(board)
        else:
            player_move(board, current_name, current_icon)

        # check for a Winner
        if check_winner(board, current_icon):
            print_board(board)
            print(f"Game Over! Congratulations {current_name} wins!")
            if current_name == player1:
                player1_score += 1
            else:
                player2_score += 1
            break

        # checking for a tie
        if is_tie(board):
            print_board(board)
            print("It's a tie! No one wins.")
            draws += 1
            break

        #switching players
        current_name = switch_player(player1, current_name, player2)

#switching icons
        if current_icon == X:
           current_icon = O
           current_name = player1
        else:
           current_icon = X
           current_name = player2

#telling python to play a game and ask for replay
while True:
    play_game()
    # printing the score
    print(f"The current score is {player1_score} and {player2_score} with {draws} ties.")

    # If replay_game returns False, stop the loop
    if not replay_game():
        break