import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNER_GAME_COUNT = 5


def prompt(message):
    print(f'==> {message}')

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
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
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt('Sorry, that is not a valid choice.')

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_square(board)) == 0:
        return None

    square = comp_find_at_risk(board)
    if square is None:
        square = random.choice(empty_square(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_square(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))


def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def join_or(numbers, seperator=', ', word='or'):
    if len(numbers) == 0:
        return ''
    elif len(numbers) == 1:
        return str(numbers[0])
    elif len(numbers) == 2:
        return f'{numbers[0]} {word} {numbers[1]}'
    else:
        return f"{seperator.join(str(num) for num in numbers[:-1])}{seperator}{word} {numbers[-1]}"

def comp_find_at_risk(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    for line in winning_lines:
        values = [board[key] for key in line]
        count = values.count(HUMAN_MARKER)
        if count == 2:
            for index, value in enumerate(values):
                if value == ' ':
                    return line[index]
    return None



board = initialize_board()

def play_tictactoe():
    player_win_count = 0
    computer_win_count = 0

    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)    

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        if detect_winner(board) == 'Player':
            player_win_count += 1
        if detect_winner(board) == 'Computer':
            computer_win_count += 1

        if player_win_count == WINNER_GAME_COUNT:
            print(f'Player wins {player_win_count} - {computer_win_count}')
        elif computer_win_count == WINNER_GAME_COUNT:
            print(f'Computer wins {computer_win_count} - {player_win_count}')

        prompt("Play again? (y or n)")
        answer = input().lower()
        if computer_win_count == WINNER_GAME_COUNT or player_win_count == WINNER_GAME_COUNT:
                prompt('Thanks for playing Tic Tac Toe!')

        if answer[0] != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tictactoe()