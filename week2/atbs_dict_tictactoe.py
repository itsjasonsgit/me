ttt_board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

# A loop with 9 possible turns
for i in range(9):
    # Print the current stage of the game with each loop
    print_board(ttt_board)
    print(turn + ', please pick a space:')
    
    move = input()
    
    # The ttt_board's move key, given by the current
    # player, is set a value of whoever's turn it is
    ttt_board[move] = turn 
    
    # Turn swapper. If it's X's turn, then make it O's turn.
    # Otherwise it's X's turn.
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_board(ttt_board)
