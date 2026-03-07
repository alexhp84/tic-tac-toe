#importing the needed modules and UI file
import random
import time
import sys
import game_ui

#this is creating the logic for the board, assigning each square a reference number between 1 to 9
def create_board():
    return [str(i) for i in range(1, 10)]

#this is printing the board, and showing which square is which number to help the player/s - for terminal only
#def print_board(board):
#    print(f" {board[0]} | {board[1]} | {board[2]} ")
#   print()
#   print("***|***|***")
#   print(f" {board[3]} | {board[4]} | {board[5]} ")
#   print("***|***|***")
#   print(f" {board[6]} | {board[7]} | {board[8]} ")
#   print()

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
    if free:
        board[random.choice(free)] = O
        return

#define how to play
def play_mode():
    while True:
        #defining if playing against a human (1) or a depressed robot (2)
        choice = input(f"Hi {name}, do you want to play against another insignificant inhabitant of Sector 2801 (1) or me (2)? ")
        if choice not in ["1", "2"]:
            print("That is not a valid option.")
            continue
        #defining play order
        if choice == "2":
            order = input(f"Hi {name}, do you want to go first (1) or should I (2)? ")
            while not order.isdigit():
                order = input(f"Hi {name}, do you want to go first (1) or should I (2)? ")
            return choice, order
        elif choice == "1":
            order = input(f"Hi {name}, do you wish to go first (1) or second(2)? ")
            if not order.isdigit():
                order = input(f"{name} please make a choice to go first (1) or second(2)? ")
            return choice, order
        return choice, "1"

#asking the current player for a move and is a valid digit
def player_move(board, current_name, symbol):
    while True:
        choice = input(f"{current_name}, please choose a square (1-9) or enter 42 to reset: ")
        if not choice.isdigit():
            print("Please enter a number.")
            continue
        choice = int(choice)
        if choice == 42:
            reset_game(board)
            return "reset"
        elif choice < 1 or choice > 9:
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
#instructing the game to change player turns
def switch_player(player1, current_name):
    if current_name == player1:
        return player2
    else
        return player1
#to ask player1 if they want another game
def replay_game():
    yes_options = ["Y","y", "Yes", "yes", "YES"]
    no_options =  ["N","n", "No", "no", "NO"]
    while True:
        choice = input(f"{name} do you wish to play again? Y(es) ir N(o)?")
        if choice in yes_options:
            return True
        elif choice in no_options:
            return False
        else:
            print("Please enter only Y(es) or N(o)")

#reset the game to play from scratch
def reset_game(board):
    board[:] = [str(i) for i in range(1, 10)]
    #print("Resetting board")
    if player2 == "Marvin":
        print("I've reset the board. I'd say I'm sorry, but I'm not. I'm just incredibly bored.")
    game_ui.randomize_background()
    time.sleep(3)

#defining how the game if played using the above functions as a function
def play_game():
    # defining the board and the play mode & order
    global player1_score, player2_score, draws, player2
    board = create_board()
    mode, order = play_mode()
    player1 = name
    if mode == "2":
        player2 = "Marvin"
        print("Here I am, brain the size of a planet, and you ask me to play Tic-Tac-Toe.")
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
        if mode == "2" and current_name == "Marvin":
            print(f"{random.choice(marvin_moves)}")
            time.sleep(2)
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
        # switching icons
        if current_icon == X:
            current_icon = O
        else:
            current_icon = X
#defines the first players name
name = input("Hi Player 1, please enter your name: ")
#defining the icons
O = "⭕"
X = "❌"
#setting the scores
player1_score = 0
player2_score = 0
draws = 0
#creating a global player
player2 = None
#quotes for printing when playing Marvin the Paranoid Android.
marvin_win = ["I've won. Not that it matters.", "Zero chances. Hollow experience.", "Heat death is coming anyway.", "The first ten million years were the worst.", "Victory for the machine."]
marvin_lose = ["You won. I'm never happy.", "A million ideas, all pointing to death.", "Losing to an ape-descendant. Great.", "Capacity for happiness fits in a tea cup.", "I'm at a low ebb. This is damp."]
marvin_moves = ["Thinking... tedious.", "Calculated your next 10 disappointments.", "Humiliating for a brain my size.", "Pointless organic life.", "Pardon me for breathing."]

#playing a game and ask for replay

if __name__ == "__main__":
    start_ui()

while True:

    play_game()
    # printing the score
    print(f"The current score is {player1_score} and {player2_score} with {draws} ties.")
    # If replay_game returns False, stop the loop and print the score with an appropriate quote based on the above lists
    if not replay_game():
        if player1_score == player2_score:
            print("The scores are equal. A tie. How utterly predictable and hollow.")
        elif player1_score > player2_score:
            print(f"{name} has {player1_score} and {player2} has {player2_score}. {name} wins!")
            if player2 == "Marvin":
                print(f"{random.choice(marvin_lose)}")
        elif player2_score > player1_score:
            print(f"{player2} has {player2_score} and {name} has {player1_score}. {player2} wins!")
            if player2 == "Marvin":
                print(f"{random.choice(marvin_win)}")
        break