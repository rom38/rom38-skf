# %%
# --- XO game for practical work on SkillFactory FPW-2.0 course
# --- Evgeniy Ivanov, flow FPW-42, Okt'2021

# - Game board for print
from itertools import product
from unittest.runner import _ResultClassType
BOARD = {7: '_', 8: '_', 9: '_',
         4: '_', 5: '_', 6: '_',
         1: '_', 2: '_', 3: '_'}

PLAYERS = {
    'X': [],  # - Cells for X-sign
    'O': []   # - Cells for O-sign
}

WIN_RULES = (
    (7, 8, 9),  # - top horizontal line
    (4, 5, 6),  # - middle  horizontal line
    (1, 2, 3),  # - bottom horizontal line
    (1, 4, 7),  # - left vertical line
    (2, 5, 8),  # - middle vertical line
    (3, 6, 9),  # - right vertical line
    (3, 5, 7),  # - \ line
    (1, 5, 9)   # - / line
)


def print_board():
    print(f'{BOARD[7]} {BOARD[8]} {BOARD[9]}')
    print(f'{BOARD[4]} {BOARD[5]} {BOARD[6]}')
    print(f'{BOARD[1]} {BOARD[2]} {BOARD[3]}')


def win_check(sign):
    board_mask = set(PLAYERS[sign])
    winner = bool([True for rule in WIN_RULES if len(
        board_mask.intersection(rule)) == 3])
    return winner


def set_cell(cell, sign):
    BOARD[cell] = sign
    PLAYERS[sign].append(cell)


def start():
    sign = 'X'  # - current sign
    step = 1    # - current step
    while True:
        # - print current game board
        print_board()

        # - wait & check user input
        cell = input(f'\nCurrent {sign}, Type cell [1-9] or 0 for exit game: ')

        # - if 0 - exit
        if cell == '0':
            break

        # - if in range [1-9] proceed game process
        elif cell in list(map(str, range(1, 10))):
            # - If cell is not busy then set current sign to it
            if BOARD[int(cell)] == '_':
                set_cell(int(cell), sign)
            else:
                print(f'\nCell is busy... repeat input')
                continue
            # - Winner check
            if win_check(sign):
                print(f'\nSign {sign} winner!!!')
                print_board()
                break
            else:
                # - If no winner, check steps
                if step == 9:
                    print(f'\nNo more steps!!! GAME OVER')
                    print_board()
                    break
                else:
                    step += 1
            # - Replace current sign
            sign = 'O' if sign == 'X' else 'X'

        # - if otherwise print a warning and continue
        else:
            print(
                '\nWrong input: Must be [1-9] for select cell, or 0 for exit game')
            continue


if __name__ == '__main__':
    print(f'\nWelcome to XO-game. Game play step by step, from X to O sign.')
    print(f'Use Numpad for select cell. Good luck!!!\n')
    start()
# %%


def won(c, n):
    if c[0] == n and c[1] == n and c[2] == n:
        return 1
    if c[3] == n and c[4] == n and c[5] == n:
        return 1
    if c[6] == n and c[7] == n and c[8] == n:
        return 1

    if c[0] == n and c[3] == n and c[6] == n:
        return 1
    if c[1] == n and c[4] == n and c[7] == n:
        return 1
    if c[2] == n and c[5] == n and c[8] == n:
        return 1

    if c[0] == n and c[4] == n and c[8] == n:
        return 1
    if c[2] == n and c[4] == n and c[6] == n:
        return 1

    return 0


pc = [' ', 'x', 'o']
c = [0] * 9
for c[0] in range(3):
    for c[1] in range(3):
        for c[2] in range(3):
            for c[3] in range(3):
                for c[4] in range(3):
                    for c[5] in range(3):
                        for c[6] in range(3):
                            for c[7] in range(3):
                                for c[8] in range(3):
                                    countx = sum([1 for x in c if x == 1])
                                    county = sum([1 for x in c if x == 2])
                                    if abs(countx-county) < 2:
                                        if won(c, 1) + won(c, 2) == 1:
                                            print("="*11)
                                            print(" %s | %s | %s" %
                                                  (pc[c[0]], pc[c[1]], pc[c[2]]))
                                            print("---+---+---")
                                            print(" %s | %s | %s" %
                                                  (pc[c[3]], pc[c[4]], pc[c[5]]))
                                            print("---+---+---")
                                            print(" %s | %s | %s" %
                                                  (pc[c[6]], pc[c[7]], pc[c[8]]))
                                            #print ("="*11)
# %%


def won(c, n):
    if c[0] == n and c[1] == n and c[2] == n:
        return 1
    if c[3] == n and c[4] == n and c[5] == n:
        return 1
    if c[6] == n and c[7] == n and c[8] == n:
        return 1

    if c[0] == n and c[3] == n and c[6] == n:
        return 1
    if c[1] == n and c[4] == n and c[7] == n:
        return 1
    if c[2] == n and c[5] == n and c[8] == n:
        return 1

    if c[0] == n and c[4] == n and c[8] == n:
        return 1
    if c[2] == n and c[4] == n and c[6] == n:
        return 1

    return 0


pc = [' ', 'x', 'o']
c = [0] * 9

for c in product(range(3), repeat=9):
    countx = sum([1 for x in c if x == 1])
    county = sum([1 for x in c if x == 2])
    if abs(countx-county) < 2 and countx >= county and won(c, 1) + won(c, 2) == 1:
        # if won(c,1) + won(c,2) == 1:
        print("="*11)
        print(" %s | %s | %s" % (pc[c[0]], pc[c[1]], pc[c[2]]))
        print("---+---+---")
        print(" %s | %s | %s" % (pc[c[3]], pc[c[4]], pc[c[5]]))
        print("---+---+---")
        print(" %s | %s | %s" % (pc[c[6]], pc[c[7]], pc[c[8]]))
# %%

# - Game board for print
BOARD = {1: '1', 2: '2', 3: '3',
         4: '4', 5: '5', 6: '6',
         7: '7', 8: '8', 9: '9', }

PLAYERS = {
    'X': [],  # - Cells for X-sign
    'O': []   # - Cells for O-sign
}

WIN_RULES = (
    (7, 8, 9),  # - top horizontal line
    (4, 5, 6),  # - middle  horizontal line
    (1, 2, 3),  # - bottom horizontal line
    (1, 4, 7),  # - left vertical line
    (2, 5, 8),  # - middle vertical line
    (3, 6, 9),  # - right vertical line
    (3, 5, 7),  # - \ line
    (1, 5, 9)   # - / line
)

def print_board(BOARD:dict):
    "Печать доски"
    print ("="*11)
    print(f' {BOARD[1]} | {BOARD[2]} | {BOARD[3] }')
    print("---+"*2+"---")
    print(f' {BOARD[4]} | {BOARD[5]} | {BOARD[6]} ')
    print("---+"*2+"---")
    print(f' {BOARD[7]} | {BOARD[8]} | {BOARD[9]} ')
    print ("="*11)

def greet():
    print("Приветствуем вас в  приложении")
    print("------------------------------")
    print("------ Крестики нолики--------")
    print("------------------------------")
    print("- Вам необходимо поочередно  -")
    print("- вводить номер клеточки     -")
    print("- куда игроки будут записы-  -")
    print("- вать крестики и нолики.    -")
    print("- Игрок играющий за крестики -")
    print("- начинает ход первым.       -")
    print("------------------------------")
    print("------------------------------")
    print("        Режимы работы:        ")
    print("------------------------------")
    print(" 1.  Человек - Человек               ")
    print(" 2.  Человек крестик -  Бот нолик    ")
    print(" 2.  Человек нолик   -  Бот крестик  ")
    print(" 3.  Бот - Бот                       ")
    print(" 4.  Выйти из программы              ")
    print("-----------------------------")
    print(" Формат ввода даты: YY-MM-DD ")

def ask_mode():
    print("-----------------------------")
    return input("    Выберите режим работы:   ")

def BOARD_unset_fields_to_list(BOARD:dict):
    "Создает список незанятых клеточек"
    result = ""
    for i in BOARD.values():
        if str(i) in '123456789':
            result+=str(i)
    return result


def ask_num(BOARD: dict):
    number = None
    while number is None:
        num_str =  input("  Введите номер:             ")
        if num_str.isdigit() and num_str in '123456789':
            if num_str in BOARD_unset_fields_to_list(BOARD):
                number = int(num_str)
            else:
                print(" Введенный вами номер клеточки занят!")
        else:
            print(" Вы ввели некорректный номер!")
            continue
    return number



greet()
BOARD[3]='X'
print(BOARD_unset_fields_to_list(BOARD))
print(ask_num(BOARD))
print_board(BOARD)

# %%
