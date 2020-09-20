board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# GLOBAL VARIABLES
player = 'x'
game_over = False
winner = None


def show_board():

    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def check():

    global game_over
    global winner

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    digonal1 = board[0] == board[4] == board[8] != '-'
    digonal2 = board[2] == board[4] == board[6] != '-'

    if row1 or col1 or digonal1:
        game_over = True
        winner = board[0]
    elif row2 or col2 or digonal2:
        game_over = True
        winner = board[4]
    elif row3 or col3:
        game_over = True
        winner = board[8]


def change_player():

    global player

    if player == 'x':
        player = 'o'
    else:
        player = 'x'


def play_game():

    global player
    global game_over
    global winner

    turns = 1
    while turns <= 9:

        show_board()

        print('Player ' + player+': mark your '+player)

        position_of_mark = int(input())

        while position_of_mark not in range(1, 10):

            print('Please give the postion as a valid number between 1-9')
            position_of_mark = int(input())

        board[position_of_mark-1] = player

        check()

        if game_over:
            print(winner + ' WON!')
            break

        if turns == 9:
            print('It is a Tie!')
            show_board()
            break

        change_player()

        turns = turns + 1

        print('--------------------------------')
        print('--------------------------------')


play_game()
