import sys
from random import randint

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship! Press q to quit at any time."
print_board(board)

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ship_row1 = random_row(board)
ship_col1 = random_row(board)
battleship1 = 0

ship_row2 = random_col(board)
ship_col2 = random_col(board)
battleship2 = 0

ship_row3 = random_row(board)
ship_col3 = random_col(board)
battleship3 = 0

while ship_row1 == ship_row2 and ship_col1 == ship_col2:
    ship_row2 = random_row(board)
    ship_col2 = random_col(board)

while ship_row1 == ship_row3 and ship_col1 == ship_col3:
    ship_row3 = random_row(board)
    ship_col3 = random_col(board)

while ship_row2 == ship_row3 and ship_col2 == ship_col3:
    ship_row3 = random_row(board)
    ship_col3 = random_col(board)

def get_move(msg):
    while True:
        try:
            s = raw_input(msg)
            if s == "q":
                sys.exit(0)
            if s == "cheat code":
                print ("Ship 1 is at: ", ship_row1, ship_col1)
                print ("Ship 2 is at: ", ship_row2, ship_col2)
                print ("Ship 3 is at: ", ship_row3, ship_col3)
            guess = int(s)
            if (guess < 1) or (guess > 10):
                raise
            break
        except Exception, e:
            print "Invalid Entry",e
    return guess
#------------------------Testing--------------------------------
#print ("Ship Row 1 is:", ship_row1)
#print ("Ship Col 1 is:", ship_col1)
#print ("Ship Row 2 is:", ship_row2)
#print ("Ship Col 2 is:", ship_col2)
#---------------------------------------------------------------


for turn in range(30):
    print 'You are on turn: ', turn + 1
    guess_row = get_move("Guess Row: ")
    guess_col = get_move("Guess Col: ")
    if guess_row == ship_row1 and guess_col == ship_col1:
        print "Congratulations! You sunk my 1st battleship!"
        battleship1 = 1
        board[guess_row - 1][guess_col - 1] = '1'

    elif guess_row == ship_row2 and guess_col == ship_col2:
        print "Congratulations! You sunk my 2nd battleship!"
        battleship2 = 1
        board[guess_row - 1][guess_col - 1] = '2'
    
    elif guess_row == ship_row3 and guess_col == ship_col3:
        print "Congratulations! You sunk my 3rd battleship!"
        battleship3 = 1
        board[guess_row - 1][guess_col - 1] = '3'

    else:
        if(board[guess_row - 1][guess_col - 1] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
    if (battleship1 == 1) and (battleship2 == 1) and (battleship3 == 1):
        print "You won!"
        print_board(board)
        break

    print_board(board)
print "Game Over"
print ("Ship 1 was at:", ship_row1, ship_col1)
print ("Ship 2 was at:", ship_row2, ship_col2)
print ("Ship 3 was at:", ship_row3, ship_col3)
board[ship_row1 - 1][ship_col1 - 1] = '1'
board[ship_row2 - 1][ship_col2 - 1] = '2'
board[ship_row3 - 1][ship_col3 - 1] = '3'
print_board(board)
