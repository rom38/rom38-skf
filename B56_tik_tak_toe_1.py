# %%

from typing import Callable


BOARD: list = [i for i in '123456789']


def print_board(BOARD: list, show_num=True):
    'Печать доски'
    BOARD2 = []

    # выключение печати цифр
    if not show_num:
        for i in BOARD:
            if i in ['X', 'O']:
                BOARD2.append(i)
            else:
                BOARD2.append(' ')
            BOARD = BOARD2

    print("="*11)
    print(f' {BOARD[0]} | {BOARD[1]} | {BOARD[2] }')
    print("---+"*2+"---")
    print(f' {BOARD[3]} | {BOARD[4]} | {BOARD[5]} ')
    print("---+"*2+"---")
    print(f' {BOARD[6]} | {BOARD[7]} | {BOARD[8]} ')
    print("="*11+'\n')


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
    print("     случайный метод                 ")
    print(" 3.  Человек крестик -  Бот нолик    ")
    print("     метод перебора                  ")
    print(" 4.  Бот крестик - Человек нолик-    ")
    print("     случайный метод                 ")
    print(" 5.  Бот крестик - Человек нолик-    ")
    print("     метод перебора                  ")
    print(" 6.  Бот - Бот                       ")
    print("     случайный метод                 ")
    print(" 7.  Бот - Бот                       ")
    print("     метод перебора                  ")
    print(" 0.  Выйти из программы              ")
    print("-----------------------------")


def wrong():
    print("-----------------------------")
    print(" Вы ввели некорректный режим ")


def ask_mode():
    print("-----------------------------")
    return input(" Выберите режим работы:   ")


def BOARD_unset_fields_to_list(BOARD: list):
    "Создает список незанятых клеточек"
    result = ""
    for i in BOARD:
        if i in '123456789':
            result += i
    return result


def ask_num(BOARD: list, sign: str):
    number = None
    while number is None:
        num_str = input(
            f"Введите номер ячейки для {sign} от 1 до 9, либо 0 для выхода из игры: ")
        print()
        if num_str.isdigit() and num_str in '0123456789':
            if num_str in BOARD_unset_fields_to_list(BOARD) or num_str == '0':
                number = int(num_str)
            else:
                print(" Введенный вами номер клеточки занят!\n")
        else:
            print(" Вы ввели некорректный номер!\n")
            continue
    return number


def win_check(BD: list, sign: str):
    'проверка выигрыша'

    # приведем список к строке
    BDS = ''.join(BD)
    # утроим знак
    sign = sign*3
    # компактная проверка
    if any(map(lambda x: x == sign,
               [BDS[0:3],   BDS[3:6],   BDS[6:9],     # по горизонтале
                BDS[0:7:3], BDS[1:8:3], BDS[2:9:3],   # по вертикали
                BDS[0:9:4], BDS[2:7:2]])):            # по диагонали
        return True
    else:
        return False


def turn_cmp(BOARD: list, sign: str, step: int):
    # проверка на выигрыш
    if win_check(BOARD, sign):
        print(f'Sign {sign} winner!!!')
        print(f'Знак {sign} победил!!!\n')
        print(' Текущая игра окончена\n')
        return False
    if len([i for i in BOARD if i not in "XO"]) == 0:
        print('Ходов больше нет! Игра окончена!\n')
        return False
    return True


def turn_bot_rnd(board: list):
    "Случайный ход бота"
    from random import choice
    free_cells = [i for i in board if i not in "XO"]
    if not free_cells:
        print("Все клетки заняты не могу ходить!")
    return int(choice(free_cells))-1


def start_HH(BOARD: list):
    # - current sign
    sign = 'X'
    # - current sign
    step = 1
    while True:
        # print current game board
        print_board(BOARD)

        # wait & check user input
        cell = ask_num(BOARD, sign)-1

        # if 0 - exit
        if cell+1 == 0:
            print(' Выход из текущей игры \n')
            break

        # - if in range [1-9] proceed game process
        BOARD[cell] = sign
        if not turn_cmp(BOARD, sign, step):
            break
        step += 1
        # Replace current sign
        # смена текущего знака
        sign = 'O' if sign == 'X' else 'X'


def start_HXBR(BOARD: list):
    # - current sign
    sign = 'X'
    # - current sign
    step = 1
    while True:
        # - print current game board
        print_board(BOARD)

        # - wait & check user input
        cell = ask_num(BOARD, sign)-1

        # - if 0 - exit
        if cell+1 == 0:
            print(' Выход из текущей игры \n')
            break

        # - if in range [1-9] proceed game process
        else:
            BOARD[cell] = sign
            if not turn_cmp(BOARD, sign, step):
                break
            step += 1
            # Replace current sign
            # смена текущего знака
            sign = 'O' if sign == 'X' else 'X'

            # Bot turn
            print(" Ход бота!")
            print_board(BOARD)
            cell = turn_bot_rnd(BOARD)
            BOARD[cell] = sign
            if not turn_cmp(BOARD, sign, step):
                break
            step += 1
            sign = 'O' if sign == 'X' else 'X'

def start_BB(BOARD: list, turn_func: Callable):
    # - current sign
    free_cells = [i for i in BOARD if i not in "XO"]
    step = 9 - len(free_cells)
    # определяем знак следующего хода
    sign = 'X' if step % 2 == 0 else 'O'
    print(" Исходная доска")
    print_board(BOARD)
    for cell in free_cells:
        print(f" Ход бота! {sign}")
        cell = turn_func(BOARD)
        BOARD[cell] = sign
        print_board(BOARD)
        if not turn_cmp(BOARD, sign, step):
            break
        # смена текущего знака
        sign = 'O' if sign == 'X' else 'X'


def turn_bot_pereb(BOARD: list, num_comb=1000):
    '''Функция берет на вход доску, симулирует 
    1000 игр, и выдает оптимальный номер ячейки'''

    win_dict = {}
    ind_win = ''
    ind_bal = ''
    BOARD = BOARD.copy()
    free_cells = [i for i in BOARD if i not in "XO"]
    step = 9 - len(free_cells)
    # определяем знак следующего хода
    sign = 'X' if step % 2 == 0 else 'O'
    # последоватьлно ставим следующий знак в свободные ячейки
    for cell in free_cells:
        win_dict[cell] = [0, 0, 0]
        BOARD_2 = BOARD.copy()
        sign_2 = sign
        BOARD_2[int(cell)-1] = sign_2
        # step_2 = step + 1
        if win_check(BOARD_2, sign_2) and sign_2 == 'X':
            win_dict[cell][0] += 1
            break
        if win_check(BOARD_2, sign_2) and sign_2 == 'O':
            win_dict[cell][1] += 1
            break
        if len([i for i in BOARD_2 if i not in "XO"]) == 0:
            win_dict[cell][2] += 1
            break
        sign_2 = 'X' if sign_2 == 'O' else 'O'
        # перебор num_comb случайных комбинаций
        for _ in range(num_comb):
            x_win, o_win, xo_win = sim_game(BOARD_2)
            win_dict[cell][0] += x_win
            win_dict[cell][1] += o_win
            win_dict[cell][2] += xo_win
    print(win_dict)
    cmp_var = 0
    cmp_bal = 0
    for ind in win_dict.items():
        if sign == 'X':
            if cmp_var <= ind[1][0]:
                cmp_var = ind[1][0]
                ind_win = ind[0]
        if sign == 'O':
            if cmp_var <= ind[1][1]:
                cmp_var = ind[1][1]
                ind_win = ind[0]
        if cmp_bal <= ind[1][2]:
            cmp_bal = ind[1][2]
            ind_bal = ind[0]
    if cmp_bal > cmp_var:
        return int(ind_bal)-1
    print(ind_win)
    return int(ind_win)-1


def sim_game(BOARD):
    x_win, o_win, xo_win = 0, 0, 0
    BOARD_2 = BOARD.copy()
    free_cells = [i for i in BOARD_2 if i not in "XO"]
    step = 9 - len(free_cells)
    sign = 'X' if step % 2 == 0 else 'O'
    for _ in free_cells:
        cell_3 = turn_bot_rnd(BOARD_2)
        BOARD_2[cell_3] = sign
        if win_check(BOARD_2, sign) and sign == 'X':
            x_win += 1
            break
        if win_check(BOARD_2, sign) and sign == 'O':
            o_win += 1
            break
        if len([i for i in BOARD_2 if i not in "XO"]) == 0:
            xo_win += 1
            break
        sign = 'X' if sign == 'O' else 'O'
    return x_win, o_win, xo_win
# %%
# start_HH()


def loop():
    greet()

    while True:
        BOARD: list = [i for i in '123456789']
        mode = ask_mode()
        if mode == "1":
            start_HH(BOARD)
        elif mode == "2":
            start_HXBR(BOARD)
            # data.append(ask_spend())
        elif mode == "3":
            pass
        elif mode == "4":
            pass
        elif mode == "5":
            pass
        elif mode == "6":
            start_BB(BOARD, turn_bot_rnd)
        elif mode == "7":
            start_BB(BOARD, turn_bot_pereb)
        elif mode == "0":
            print(' Выход из программы\n')
            break
        else:
            wrong()


# %%
if __name__ == '__main__':

    loop()

# %%


def start_BBR2(BOARD: list):
    # - current sign
    sign = 'X'
    # - current sign
    step = 1
    while True:
        # print current game board

        # wait & check user input
        cell = turn_bot_rnd(BOARD)
        print(f" Ход бота! {sign}")

        BOARD[cell] = sign
        if not turn_cmp(BOARD, sign, step):
            break
        step += 1
        # Replace current sign
        # смена текущего знака
        sign = 'O' if sign == 'X' else 'X'

        # Bot turn
        print(f" Ход бота! {sign}")
        cell = turn_bot_rnd(BOARD)
        BOARD[cell] = sign
        if not turn_cmp(BOARD, sign, step):
            break
        step += 1
        sign = 'O' if sign == 'X' else 'X'
    print_board(BOARD, show_num=False)

# %%


BOARD = list('X23XO6789')
print(turn_bot_pereb(BOARD))


# %%
