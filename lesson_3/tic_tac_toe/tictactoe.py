import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f'==> {message}')

def display_board(board):

    print('')
    print('       |        |        ')
    print(f"    {board[1]}  |    {board[2]}   |  {board[3]}")
    print('       |        |        ')
    print('-------+--------+--------')
    print('       |        |        ')
    print(f"    {board[4]}  |    {board[5]}   |  {board[6]}")
    print('       |        |        ')
    print('-------+--------+--------')
    print('       |        |        ')
    print(f"    {board[7]}  |    {board[8]}   |  {board[9]}")
    print('       |        |        ')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}

def empty_square(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

board = {
  1: ' ', # top left
  2: ' ', # top center
  3: ' ', # top right
  4: ' ', # middle left
  5: ' ', # center
  6: ' ', # middle right
  7: ' ', # bottom left
  8: ' ', # bottom center
  9: ' ',  # bottom right
}

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_square(board)]
        prompt(f"Choose a square ({', '.join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt('Sorry, that is not a valid choice.')

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_square(board)) == 0:
        return
    square = random.choice(empty_square(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_square(board)) == 0

def someone_won(board):
    return False





board = initialize_board()
display_board(board)

while True:
    player_chooses_square(board)
    computer_chooses_square(board)
    display_board(board)

    if someone_won(board) or board_full(board):
        break