import random
import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen_width = 600
screen_height = 600

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-Tac-Toe')

line_width = 12
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def draw_board():
    bg = (93, 188, 210)
    grid = (25, 121, 169)
    window.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(window, grid, (0, x * 200),
                         (screen_width, x * 200), line_width)
        pygame.draw.line(window, grid, (x * 200, 0),
                         (x * 200, screen_height), line_width)


def computer():
    if result(board):
        return

    if computer_attack():
        return

    if computer_defend():
        return

    while True:
        if result(board):
            break

        row = random.choice([0, 1, 2])
        col = random.choice([0, 1, 2])

        if empty_place(row, col):
            board[row][col] = 'O'
            break
    return


def computer_defend():
    for row in range(0, 3):
        if board[row][0] == 'X' and board[row][1] == 'X':
            if empty_place(row, 2):
                board[row][2] = 'O'
                return True
        if board[row][1] == 'X' and board[row][2] == 'X':
            if empty_place(row, 0):
                board[row][0] = 'O'
                return True
        if board[row][0] == 'X' and board[row][2] == 'X':
            if empty_place(row, 1):
                board[row][1] = 'O'
                return True

    for col in range(0, 3):
        if board[0][col] == 'X' and board[1][col] == 'X':
            if empty_place(2, col):
                board[2][col] = 'O'
                return True
        if board[1][col] == 'X' and board[2][col] == 'X':
            if empty_place(0, col):
                board[0][col] = 'O'
                return True
        if board[0][col] == 'X' and board[2][col] == 'X':
            if empty_place(1, col):
                board[1][col] = 'O'
                return True

    if board[0][0] == 'X' and board[1][1] == 'X':
        if empty_place(2, 2):
            board[2][2] = 'O'
            return True
    if board[1][1] == 'X' and board[2][2] == 'X':
        if empty_place(0, 0):
            board[0][0] = 'O'
            return True
    if board[0][0] == 'X' and board[2][2] == 'X':
        if empty_place(1, 1):
            board[1][1] = 'O'
            return True

    if board[0][2] == 'X' and board[1][1] == 'X':
        if empty_place(2, 0):
            board[2][0] = 'O'
            return True
    if board[1][1] == 'X' and board[2][0] == 'X':
        if empty_place(0, 2):
            board[0][2] = 'O'
            return True
    if board[0][2] == 'X' and board[2][0] == 'X':
        if empty_place(1, 1):
            board[1][1] = 'O'
            return True

    return False


def computer_attack():
    for row in range(0, 3):
        if board[row][0] == 'O' and board[row][1] == 'O':
            if empty_place(row, 2):
                board[row][2] = 'O'
                return True
        if board[row][1] == 'O' and board[row][2] == 'O':
            if empty_place(row, 0):
                board[row][0] = 'O'
                return True
        if board[row][0] == 'O' and board[row][2] == 'O':
            if empty_place(row, 1):
                board[row][1] = 'O'
                return True

    for col in range(0, 3):
        if board[0][col] == 'O' and board[1][col] == 'O':
            if empty_place(2, col):
                board[2][col] = 'O'
                return True
        if board[1][col] == 'O' and board[2][col] == 'O':
            if empty_place(0, col):
                board[0][col] = 'O'
                return True
        if board[0][col] == 'O' and board[2][col] == 'O':
            if empty_place(1, col):
                board[1][col] = 'O'
                return True

    if board[0][0] == 'O' and board[1][1] == 'O':
        if empty_place(2, 2):
            board[2][2] = 'O'
            return True
    if board[1][1] == 'O' and board[2][2] == 'O':
        if empty_place(0, 0):
            board[0][0] = 'O'
            return True
    if board[0][0] == 'O' and board[2][2] == 'O':
        if empty_place(1, 1):
            board[1][1] = 'O'
            return True

    if board[0][2] == 'O' and board[1][1] == 'O':
        if empty_place(2, 0):
            board[2][0] = 'O'
            return True
    if board[1][1] == 'O' and board[2][0] == 'O':
        if empty_place(0, 2):
            board[0][2] = 'O'
            return True
    if board[0][2] == 'O' and board[2][0] == 'O':
        if empty_place(1, 1):
            board[1][1] = 'O'
            return True

    return False


def empty_place(row, col):
    return board[int(row)][int(col)] == ' '


def result(board):
    for row in range(0, 3):
        if board[row][0] == 'X' and board[row][1] == 'X' and board[row][2] == 'X':
            pygame.draw.line(window, (255, 0, 0), (15, row * 200 + 200//2),
                             (screen_width - 15, row * 200 + 200//2), 12)
            return 'X'

        if board[row][0] == 'O' and board[row][1] == 'O' and board[row][2] == 'O':
            pygame.draw.line(window, (255, 0, 0), (15, row * 200 + 200//2),
                             (screen_width - 15, row * 200 + 200//2), 12)
            return 'O'

    for column in range(0, 3):
        if board[0][column] == 'X' and board[1][column] == 'X' and board[2][column] == 'X':
            pygame.draw.line(window, (255, 0, 0), (column * 200 + 200//2, 15),
                             (column * 200 + 200//2, screen_height - 15), 12)
            return 'X'

        if board[0][column] == 'O' and board[1][column] == 'O' and board[2][column] == 'O':
            pygame.draw.line(window, (255, 0, 0), (column * 200 + 200//2, 15),
                             (column * 200 + 200//2, screen_height - 15), 12)
            return 'O'

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        pygame.draw.line(window, (255, 0, 0), (15, 15),
                         (screen_width - 15, screen_height - 15), 12)
        return 'X'

    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        pygame.draw.line(window, (255, 0, 0), (15, 15),
                         (screen_width - 15, screen_height - 15), 12)
        return 'O'

    if board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        pygame.draw.line(window, (255, 0, 0),
                         (15, screen_height - 15), (screen_width - 15, 15), 12)
        return 'X'

    if board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
        pygame.draw.line(window, (255, 0, 0),
                         (15, screen_height - 15), (screen_width - 15, 15), 12)
        return 'O'

    for row in range(0, 3):
        for col in range(0, 3):
            if empty_place(row, col):
                return False

    return 'Tie'


def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                pygame.draw.circle(window, (204, 231, 232), (int(
                    col * 200 + 100), int(row * 200 + 100)), 60, 15)
            if board[row][col] == 'X':
                pygame.draw.line(window, (55, 55, 55), (
                    col * 200 + 55, row * 200 + 200 - 55), (col * 200 + 200 - 55, row * 200 + 55), 25)
                pygame.draw.line(window, (55, 55, 55), (
                    col * 200 + 55, row * 200 + 55), (col * 200 + 200 - 55, row * 200 + 200 - 55), 25)


def restart():
    window.fill((93, 188, 210))
    draw_board()
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '


def game():
    draw_board()
    turn = 'player'
    game_over = False

    running = True
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                if empty_place(clicked_row, clicked_col) and not result(board):
                    if turn == 'player':
                        board[clicked_row][clicked_col] = 'X'
                        turn = 'computer'

                    if turn == 'computer':
                        computer()
                        turn = 'player'

                    draw_figures()

                    if result(board):
                        s = pygame.Surface((600, 600))
                        s.set_alpha(128)
                        s.fill((255, 255, 255))
                        window.blit(s, (0, 0))
                        if result(board) == 'X':
                            winner = myfont.render(
                                'Player Won!', False, (0, 34, 255))
                            window.blit(winner, (220, 275))

                        elif result(board) == 'O':
                            winner = myfont.render(
                                'Computer Won!', False, (0, 34, 255))
                            window.blit(winner, (196, 275))

                        elif result(board) == 'Tie':
                            winner = myfont.render(
                                'Tie!', False, (0, 34, 255))
                            window.blit(winner, (275, 275))

                        again = myfont.render(
                            'Press R to Restart', False, (0, 34, 255))
                        window.blit(again, (175, 350))

                        game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    turn = 'player'
                    game_over = False

        pygame.display.update()


game()
