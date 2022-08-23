# %%
import random


class BoardExeption(Exception):
    pass


class ShipOutBoard(BoardExeption):
    pass


class DotOutBoard(BoardExeption):
    pass


class Dot():
    def __init__(self, x: int, y: int) -> None:
        if not (1 <= x <= 6 and
                1 <= y <= 6):
            raise DotOutBoard('координаты точки выходят за'
                              'границы доски')
        self.x = x
        self.y = y

    def __eq__(self, alt_dot: 'Dot'):
        if not isinstance(alt_dot, Dot):
            raise ValueError("Передано неправильное значение")
            # return False
        if self.x == alt_dot.x and self.y == alt_dot.y:
            return True
        return False

    def __hash__(self):
        return hash(f"dot {self.x}{self.y}")

    def near(self):
        dots_near: list = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if not (1 <= self.x + i <= 6 and
                        1 <= self.y + j <= 6):
                    continue
                dots_near.append(Dot(self.x + i, self.y + j))
        return dots_near

    def __repr__(self) -> str:
        return f'Dot(x={self.x}, y={self.y})'


class Ship():
    sh_len: int
    nos: Dot
    vrt_hrz: bool
    life: int

    def __init__(self, nos: Dot, sh_len: int, vrt_hrz: bool):
        if ((vrt_hrz and nos.y + sh_len > 6) or
                (not vrt_hrz and nos.x + sh_len > 6) or
                sh_len < 0):
            raise ShipOutBoard('координаты корабля выходят за'
                               'границы доски')
        self.nos = nos
        self.sh_len = sh_len
        self.vrt_hrz = vrt_hrz

    def dots(self):
        dots_sh = []
        for i in range(self.sh_len):
            if self.vrt_hrz:
                dots_sh.append(Dot(self.nos.x, self.nos.y+i))
            else:
                dots_sh.append(Dot(self.nos.x+i, self.nos.y))
        return dots_sh

    def cont(self):
        cont_sh = []
        for dot_sh in self.dots():
            for dot_nr in dot_sh.near():
                cont_sh.append(dot_nr)
        return list(set(cont_sh)-set(self.dots()))


class Board():
    map_br: list[list[str]]
    ships: list[Ship]
    hid: bool
    live_ships: int

    def __init__(self):
        self.map_br = []
        self.ships = []
        for y in range(6):
            self.map_br.append([])
            for x in range(6):
                self.map_br[y].append("O")

    def show_ships(self):
        for ship in self.ships:
            for i in ship.dots():
                self.map_br[i.y-1][i.x-1] = '■'

    def show_cont(self):
        'отображение контуров кораблей'
        for ship in self.ships:
            for i in ship.cont():
                self.map_br[i.y-1][i.x-1] = 'N'

    def add_ship(self, ship: Ship):
        self.ships.append(ship)

    def contour(self):
        pass

    def show(self):
        map_vis: str = "   |"
        for xh in range(len(self.map_br[0])):
            map_vis += f" {xh+1} |"
        map_vis += '\n'
        for yn, y in enumerate(self.map_br):
            map_vis += f' {yn+1} |'
            for x in y:
                map_vis += f" {x} |"
            map_vis += '\n'
        return map_vis[:-1]

        # hid: bool
        pass

    def show_ln(self):
        return self.show().split('\n')

    def out(self) -> bool:
        # exeption out, retry
        return True

    def shot(self):
        pass

    def random_board(self):
        all_dots_orig = [Dot(x, y)
                         for x in range(1, 7)
                         for y in range(1, 7)]
        ships_def = [3, 2, 2, 1, 1, 1, 1]
        while True:
            ships = []
            all_dots = all_dots_orig.copy()
            try:
                for i, sh_len in enumerate(ships_def):
                    if not all_dots:
                        break
                    ships.append(Ship(random.choice(all_dots), sh_len,
                                      random.choice([True, False])))
                    # отнимаем от всех точек точки сгенерированного
                    # корабля и его контура
                    all_dots = (list(set(all_dots)
                                     - set(ships[i].dots())
                                     - set(ships[i].cont())))

                if len(ships) != len(ships_def):
                    continue
                all_sh_dots = [dot for ship in ships for dot in ship.dots()]
                all_sh_conts = [dot for ship in ships for dot in ship.cont()]
                # проверяем, чтобы корабли не пересекались и их
                # контуры были свободны
                if (len(all_sh_dots) == len(set(all_sh_dots)) and
                        set(all_sh_dots).isdisjoint(set(all_sh_conts))):
                    self.ships = ships
                    break
            except DotOutBoard:
                continue
            except ShipOutBoard:
                continue


class Player():
    my_board: Board
    enemy_board: Board

    def ask(self):
        pass

    def move(self):
        # return bool
        self.ask()
        try:
            self.enemy_board.shot()
        except BoardExeption:
            pass


class AI(Player):
    pass


class User(Player):

    def ask(self, BOARD):
        while True:
            coord_str = input(
                "Введите координаты клеточки через пробел "
                " от 1 до 6, либо 0 для выхода из игры: ")
            print()
            if coord_str == '0':
                return 0

            if not (len(coord_str) == 3 and
                    coord_str[1] == ' '):
                print(" Вы ввели некорректный номер!\n")
                continue
            dot_shot = Dot(*map(int, coord_str.split(' ')))
            break
            # if str(num) in BOARD_unset_fields_to_list(BOARD):
            #     break
            print(" Введенный вами номер ячейки занят!\n")
        return dot_shot


class Game():
    user: User
    user_board: Board
    ai: AI
    ai_board: Board

    def __init__(self) -> None:
        self.user_board = Board()
        self.ai_board = Board()

    def show_two_board(self):
        for y1, y2 in zip(self.user_board.show_ln(),
                          self.ai_board.show_ln()):
            print(f"{y1}       {y2}")

    def greet(self) -> str:
        greet_str = (
            "-----------Приветствуем вас в  приложении-----------------------\n"
            "----------------------------------------------------------------\n"
            "----------------- Морской бой ----------------------------------\n"
            "----------------------------------------------------------------\n"
            "- Вам необходимо поочередно указывать координаты клеточки куда -\n"
            "- будет наносится выстрел артиллерии. В случае попадания во    -\n"
            "- вражеский корабль Вам предоставляется дополнительный ход.    -\n"
            "------------------------------\n"
            "        Режимы работы:        \n"
            "------------------------------\n"
            " 1.  Человек - Человек               \n"
            " 2.  Человек крестик -  Бот нолик    \n"
            "     случайный метод                 \n"
            " 0.  Выйти из программы              \n"
            "-----------------------------")
        return greet_str

    def loop(self):
        self.user.move()

    def start(self):
        self.greet()
        self.loop()


# %%
xxx = Board()
# print(xxx.map_br)
print(xxx.show())
# %%
dd = Dot(1, 1)
dd.near()
# %%

ggg = Game()
ggg.user_board.add_ship(Ship(Dot(1, 1), 3, False))

ggg.user_board.add_ship(Ship(Dot(1, 3), 3, True))

ggg.user_board.random_board()
ggg.user_board.show_cont()
ggg.user_board.show_ships()

ggg.ai_board.random_board()
ggg.ai_board.show_cont()
ggg.ai_board.show_ships()


ggg.show_two_board()
# %%
shhh = Ship(Dot(1, 1), 1, True)
shhh.dots()
# %%
ggg = Game()
print(ggg.greet())

# %%
