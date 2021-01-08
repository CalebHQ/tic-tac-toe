import random
import os

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(board):
    print('-+- TIC-TAC-TOE -+-')
    print('')
    print('     0' + ' '*3 + '1' + ' '*3 + '2')
    print('')

    for row in range(0, 3):
        print(f'{row}   ', end='')
        for col in range(0, 3):
            print(f' {board[row][col]} ', end='')
            if col != 2:
                print('|', end='')
        print('')
        if row != 2:
            print('    ' + '-'*3 + '+' + '-'*3 + '+' + '-'*3)
    print('')


def player(choice):
    while True:
        if result(board):
            break

        while True:
            try:
                row = input('Row (0-2): ')
                if 0 <= int(row) <= 2:
                    break
            except ValueError:
                print('invalid row')
            print('Row doesnt exist')

        while True:
            try:
                col = input('Column (0-2): ')
                if 0 <= int(col) <= 2:
                    break
            except ValueError:
                print('invalid column')
            print('Column doesnt exist')

        if empty_place(row, col):
            board[int(row)][int(col)] = choice
            break
        print('Spot has been taken already!')


def computer(player_choice):
    if player_choice == "X":
        choice = 'O'
    else:
        choice = 'X'

    if result(board):
        return

    if computer_attack(choice):
        return

    if computer_defend(player_choice, choice):
        return

    while True:
        if result(board):
            break

        row = random.choice([0, 1, 2])
        col = random.choice([0, 1, 2])

        if empty_place(row, col):
            board[row][col] = choice
            break
    return


def computer_defend(player_choice, choice):
    for row in range(0, 3):
        if board[row][0] == player_choice and board[row][1] == player_choice:
            if empty_place(row, 2):
                board[row][2] = choice
                return True
        if board[row][1] == player_choice and board[row][2] == player_choice:
            if empty_place(row, 0):
                board[row][0] = choice
                return True
        if board[row][0] == player_choice and board[row][2] == player_choice:
            if empty_place(row, 1):
                board[row][1] = choice
                return True

    for col in range(0, 3):
        if board[0][col] == player_choice and board[1][col] == player_choice:
            if empty_place(2, col):
                board[2][col] = choice
                return True
        if board[1][col] == player_choice and board[2][col] == player_choice:
            if empty_place(0, col):
                board[0][col] = choice
                return True
        if board[0][col] == player_choice and board[2][col] == player_choice:
            if empty_place(1, col):
                board[1][col] = choice
                return True

    if board[0][0] == player_choice and board[1][1] == player_choice:
        if empty_place(2, 2):
            board[2][2] = choice
            return True
    if board[1][1] == player_choice and board[2][2] == player_choice:
        if empty_place(0, 0):
            board[0][0] = choice
            return True
    if board[0][0] == player_choice and board[2][2] == player_choice:
        if empty_place(1, 1):
            board[1][1] = choice
            return True

    if board[0][2] == player_choice and board[1][1] == player_choice:
        if empty_place(2, 0):
            board[2][0] = choice
            return True
    if board[1][1] == player_choice and board[2][0] == player_choice:
        if empty_place(0, 2):
            board[0][2] = choice
            return True
    if board[0][2] == player_choice and board[2][0] == player_choice:
        if empty_place(1, 1):
            board[1][1] = choice
            return True

    return False


def computer_attack(choice):
    for row in range(0, 3):
        if board[row][0] == choice and board[row][1] == choice:
            if empty_place(row, 2):
                board[row][2] = choice
                return True
        if board[row][1] == choice and board[row][2] == choice:
            if empty_place(row, 0):
                board[row][0] = choice
                return True
        if board[row][0] == choice and board[row][2] == choice:
            if empty_place(row, 1):
                board[row][1] = choice
                return True

    for col in range(0, 3):
        if board[0][col] == choice and board[1][col] == choice:
            if empty_place(2, col):
                board[2][col] = choice
                return True
        if board[1][col] == choice and board[2][col] == choice:
            if empty_place(0, col):
                board[0][col] = choice
                return True
        if board[0][col] == choice and board[2][col] == choice:
            if empty_place(1, col):
                board[1][col] = choice
                return True

    if board[0][0] == choice and board[1][1] == choice:
        if empty_place(2, 2):
            board[2][2] = choice
            return True
    if board[1][1] == choice and board[2][2] == choice:
        if empty_place(0, 0):
            board[0][0] = choice
            return True
    if board[0][0] == choice and board[2][2] == choice:
        if empty_place(1, 1):
            board[1][1] = choice
            return True

    if board[0][2] == choice and board[1][1] == choice:
        if empty_place(2, 0):
            board[2][0] = choice
            return True
    if board[1][1] == choice and board[2][0] == choice:
        if empty_place(0, 2):
            board[0][2] = choice
            return True
    if board[0][2] == choice and board[2][0] == choice:
        if empty_place(1, 1):
            board[1][1] = choice
            return True

    return False


def empty_place(row, col):
    if board[int(row)][int(col)] == ' ':
        return True
    return False


def result(board):
    for row in range(0, 3):
        if board[row][0] == 'X' and board[row][1] == 'X' and board[row][2] == 'X':
            return 'X'

        if board[row][0] == 'O' and board[row][1] == 'O' and board[row][2] == 'O':
            return 'O'

    for column in range(0, 3):
        if board[0][column] == 'X' and board[1][column] == 'X' and board[2][column] == 'X':
            return 'X'

        if board[0][column] == 'O' and board[1][column] == 'O' and board[2][column] == 'O':
            return 'O'

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'X'

    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 'O'

    if board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        return 'X'

    if board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
        return 'O'

    for row in range(0, 3):
        for col in range(0, 3):
            if empty_place(row, col):
                return False

    return 'Tie'


def game():
    print('NOTE: X has priority!')
    while True:
        choice = input('X or O: ').upper()
        if choice == 'X' or choice == 'O':
            break
        print('invalid choice')

    os.system('cls')

    while True:
        if choice == 'O':
            computer(choice)
            print_board(board)
            player(choice)
        else:
            print_board(board)
            player(choice)
            computer(choice)

        if result(board):
            os.system('cls')
            print_board(board)
            print('Game Over')
            break
        os.system('cls')

    if result(board) == 'Tie':
        print('TIE')
    elif choice == result(board):
        print('Player Wins!')
    else:
        print('Computer Wins!')
    print('')

    again = input('Again? (y/n): ').upper()
    if again == 'Y':
        for row in range(0, 3):
            for col in range(0, 3):
                board[row][col] = ' '
        os.system('cls')
        game()


os.system('cls')
game()
