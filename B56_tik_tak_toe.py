
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
print_board(BOARD)

num_2 = (ask_num(BOARD))

print(num_2)
BOARD[num_2]='X'


print_board(BOARD)