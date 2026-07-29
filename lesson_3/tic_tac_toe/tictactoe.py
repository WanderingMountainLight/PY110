

def display_board(board):

    print('')
    print('       |        |        ')
    print(f"    {board[1]}  |     {board[2]}  |  {board[3]}")
    # print('       |        |        ')
    print('       |        |        ')
    print('-------+--------+--------')
    print('       |        |        ')
    print(f"    {board[4]}  |    {board[5]}   |  {board[6]}")
    # print('       |        |        ')
    print('       |        |        ')
    print('-------+--------+--------')
    print('       |        |        ')
    print(f"    {board[7]}  |     {board[8]}  |  {board[9]}")
    # print('       |        |        ')
    print('       |        |        ')
    print('')




board = {
  1: 'X', # top left
  2: ' ', # top center
  3: ' ', # top right
  4: ' ', # middle left
  5: 'O', # center
  6: ' ', # middle right
  7: ' ', # bottom left
  8: ' ', # bottom center
  9: 'X',  # bottom right
}

display_board(board)