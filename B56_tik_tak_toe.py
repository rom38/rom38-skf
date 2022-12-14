# %%
# # - Game board for print
# BOARD = {1: '1', 2: '2', 3: '3',
#          4: '4', 5: '5', 6: '6',
#          7: '7', 8: '8', 9: '9', }
# - Game board for print
BOARD: list = [i for i in '123456789']

def print_board(BOARD: list, show_num=True):
    'Печать доски'
    BOARD2=[]

    # выключение печати цифр
    if not show_num:
         for i in BOARD:
            if i in ['X','O']:
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


def ask_num(BOARD: list, sign:str):
    number = None
    while number is None:
        num_str = input(f"Введите номер ячейки для {sign} от 1 до 9, либо 0 для выхода из игры: ")
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

    # # по горизонтали
    # if BDS[0:3] == sign or BDS[3:6] == sign or BDS[6:9] == sign:
    #     return True

    # # по вертикали
    # if BDS[0:7:3] == sign or BDS[1:8:3] == sign or BDS[2:9:3] == sign:
    #     return True
        
    # # по диагонали
    # if BDS[0:9:4] == sign or BDS[2:7:2] == sign:
    #     return True

    # компактная проверка
    if any(map(lambda x: x == sign,

        # по горизонтале
        [BDS[0:3], BDS[3:6], BDS[6:9],

        # по вертикали
        BDS[0:7:3], BDS[1:8:3],  BDS[2:9:3],

        # по диагонали
        BDS[0:9:4], BDS[2:7:2]])):
        return True
    else:
        return False

def turn_cmp(BOARD:list, sign:str, step:int):
     # Winner check
    # проверка на выигрыш
    if win_check(BOARD,sign):
        print(f'Sign {sign} winner!!!')
        print(f'Знак {sign} победил!!!\n')
        print_board(BOARD, show_num=False)

        # выход
        print(f' Текущая игра окончена\n')
        return False
    else:

        # If no winner, check steps
        # Если нет победителя, проверить на
        # оставшиеся ходы 
        if step == 9:
            print(f'Ходов больше нет! Игра окончена!\n')
            print_board(BOARD, show_num=False)
            return False
        else:
            step += 1
        return True

def turn_bot_rnd(board:list,sign:str):
    "Случайный ход бота"
    from random import choice
    free_cells=[i for i in board if i not in "XO"]
    return int(choice(free_cells))-1



def start_HH(BOARD:list):
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
            print(f' Выход из текущей игры \n')
            break
        
        

        # - if in range [1-9] proceed game process
        else:
            BOARD[cell] = sign
            if not turn_cmp(BOARD,sign,step):
                break
            step += 1
            # Replace current sign
            # смена текущего знака
            sign = 'O' if sign == 'X' else 'X'

# greet()
# BOARD[3-1] = 'X'
# print(BOARD_unset_fields_to_list(BOARD))
# print_board(BOARD)

# num_2 = (ask_num(BOARD)-1)

# print(num_2)
# BOARD[num_2] = 'X'


# print_board(BOARD)

def start_HXBR(BOARD:list):
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
            print(f' Выход из текущей игры \n')
            break

        # - if in range [1-9] proceed game process
        else:
            BOARD[cell] = sign
            if not turn_cmp(BOARD,sign,step):
                break
            step += 1
            # Replace current sign
            # смена текущего знака
            sign = 'O' if sign == 'X' else 'X'

            # Bot turn
            print(" Ход бота!")
            print_board(BOARD)
            cell = turn_bot_rnd(BOARD, sign)
            BOARD[cell] = sign
            if not turn_cmp(BOARD,sign,step):
                break
            step += 1
            sign = 'O' if sign == 'X' else 'X'

def start_BBR(BOARD:list):
    # - current sign
    sign = 'X' 
    # - current sign
    step = 1    
    while True:
        # - print current game board
        print_board(BOARD)

        # - wait & check user input
        cell = turn_bot_rnd(BOARD, sign)
        print(f" Ход бота! {sign}")

        BOARD[cell] = sign
        if not turn_cmp(BOARD,sign,step):
            break
        step += 1
        # Replace current sign
        # смена текущего знака
        sign = 'O' if sign == 'X' else 'X'

        # Bot turn
        print_board(BOARD)
        print(f" Ход бота! {sign}")
        cell = turn_bot_rnd(BOARD, sign)
        BOARD[cell] = sign
        if not turn_cmp(BOARD,sign,step):
            break
        step += 1
        sign = 'O' if sign == 'X' else 'X'
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
            #data.append(ask_spend())
        elif mode == "3":
            pass
        elif mode == "4":
            pass
        elif mode == "5":
            pass
        elif mode == "6":
            start_BBR(BOARD)
        elif mode == "0":
            print(f' Выход из программы\n')
            break
        else:
            wrong()
    
# %%
if __name__ == '__main__':

    loop()