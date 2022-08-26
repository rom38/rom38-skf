# %%
import random


class BoardExeption(Exception):
    pass


class ShipOutBoard(BoardExeption):
    pass


class ShotDouble(BoardExeption):
    pass


class DotOutBoard(BoardExeption):
    pass


class ExitGame(BoardExeption):
    pass


class Dot():
    x: int
    y: int

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
        self.life = sh_len

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
    # live_ships: int
    shots: list[Dot]

    def __init__(self):
        self.hid = True
        self.ships = []
        self.shots = []
        self.map_reset()

    def map_reset(self):
        'сброс карты'
        __map_etal = []
        for y in range(6):
            __map_etal.append([])
            for _x in range(6):
                __map_etal[y].append("O")
        self.map_br = __map_etal.copy()

    def show_ships(self):
        'отображение кораблей'
        for ship in self.ships:
            for i in ship.dots():
                self.map_br[i.y-1][i.x-1] = '■'

    def show_cont(self):
        'отображение контуров кораблей'
        for ship in self.ships:
            for i in ship.cont():
                self.map_br[i.y-1][i.x-1] = 'N'

    def show_shots(self):
        'отображение выстрелов'
        for shot in self.shots:
            if self.map_br[shot.y-1][shot.x-1] == 'O':
                self.map_br[shot.y-1][shot.x-1] = 'T'
            elif self.map_br[shot.y-1][shot.x-1] == '■':
                self.map_br[shot.y-1][shot.x-1] = 'X'

    def add_ship(self, ship: Ship):
        self.ships.append(ship)

    def show(self):
        map_vis: str = f"  потоплено {self.sink_ships()} из {len(self.ships)} кораблей \n"
        map_vis += "   |"
        for xh in range(len(self.map_br[0])):
            map_vis += f" {xh+1} |"
        map_vis += '\n'
        for yn, y in enumerate(self.map_br):
            map_vis += f' {yn+1} |'
            for x in y:
                map_vis += f" {x} |"
            map_vis += '\n'
        if self.hid:
            map_vis = map_vis.replace('■', 'O')
        return map_vis[:-1]

        # hid: bool
        pass

    def show_ln(self):
        return self.show().split('\n')

    def ships_dots(self):
        'возврат точек всех кораблей'
        return [dot for ship in self.ships for dot in ship.dots()]

    def plus_shot(self):
        'Дополнительный ход при попадании'
        return self.shots[-1] in self.ships_dots()

    def check_ships(self):
        'Проверка кораблей'
        for ship in self.ships:
            hits = set(self.shots) & set(ship.dots())
            if hits:
                ship.life = ship.sh_len - len(hits)

    def live_ships(self):
        self.check_ships()
        live = 0
        for ship in self.ships:
            if ship.life > 0:
                live += 1
        return live

    def sink_ships(self):
        self.check_ships()
        sink = 0
        for ship in self.ships:
            if ship.life == 0:
                sink += 1
        return sink

    def all_ships_sink(self):
        return set(self.ships_dots()).issubset(set(self.shots))

    def out(self) -> bool:
        # exeption out, retry
        return True

    def shot(self):
        self.map_reset()
        self.show_ships()
        self.show_shots()

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

    def __init__(self, my_b: Board, en_b: Board):
        self.my_board = my_b
        self.enemy_board = en_b

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
    def ask(self):
        while True:
            x = random.choice(range(1, 7))
            y = random.choice(range(1, 7))
            dot_shot = Dot(x, y)
            if dot_shot in self.enemy_board.shots:
                continue
            self.enemy_board.shots.append(dot_shot)
            break

class User(Player):

    def ask(self):
        while True:
            coord_str = input(
                "Введите координаты клеточки через пробел "
                " от 1 до 6, либо 0 для выхода из игры: ")
            print()
            if coord_str == '0':
                raise ExitGame

            if not (len(coord_str) == 3 and
                    coord_str[1] == ' '):
                print(" Вы ввели некорректный номер!\n"
                      " Повторите ввод!\n")
                continue
            dot_shot = Dot(*map(int, coord_str.split(' ')))
            if dot_shot in self.enemy_board.shots:
                raise ShotDouble('Выстрел в эту ячейку уже был!')
            self.enemy_board.shots.append(dot_shot)
            break
        if dot_shot in self.enemy_board.ships_dots():
            print('Игрок попал в корабль')
            return True
        return False


class Game():
    user: User
    user_board: Board
    ai: AI
    ai_board: Board

    def __init__(self) -> None:
        self.user_board = Board()
        self.ai_board = Board()
        self.user = User(self.user_board, self.ai_board)
        self.ai = AI(self.ai_board, self.user_board)

    def show_two_board(self):
        print(""" ---------  Игрок  ---------        -----------  AI  ----------""")
        for y1, y2 in zip(self.user_board.show_ln(),
                          self.ai_board.show_ln()):
            print(f"{y1}       {y2}")
        print()

    def greet(self) -> str:
        gr_str = (
            "-----------Приветствуем вас в  приложении----------------------\n"
            "---------------------------------------------------------------\n"
            "-------------------- Морской бой ------------------------------\n"
            "---------------------------------------------------------------\n"
            "- Вам  необходимо  поочередно указывать  координаты  клеточки -\n"
            "- куда будет наносится выстрел артиллерии. В случае попадания -\n"
            "- во вражеский корабль Вам предоставляется дополнительный ход.-\n"
            "------------------------------------------------------------\n"
            "                    Режимы работы:                          \n"
            "------------------------------------------------------------\n"
            " 1.  Начать игру                                            \n"
            " 2.  Сгенерировать новое расположение кораблей              \n"
            " 0.  Выйти из программы                                     \n"
            "-----------------------------")
        return gr_str

    def loop(self):
        for _ in range(10):
            print(self.greet())
            self.user_board.random_board()
            self.user_board.map_reset()
            self.user_board.show_ships()
            self.user_board.hid = False
            self.ai_board.random_board()
            self.ai_board.map_reset()
            self.ai_board.show_ships()
            mode = self.ask_mode()
            self.show_two_board()
            if mode == '1':
                while True:
                    try:
                        while True:
                            self.user.move()
                            if self.ai_board.all_ships_sink():
                                print('Игрок потопил все корабли!')
                                self.show_two_board()
                                raise ExitGame
                            self.show_two_board()
                            if self.user.enemy_board.plus_shot():
                                print('Игрок попал в корабль! Дополнительный ход.')
                                continue
                            break
                        print('Ход AI')
                        while True:
                            self.ai.move()
                            if self.ai_board.all_ships_sink():
                                print('Игрок потопил все корабли!')
                                self.show_two_board()
                                raise ExitGame
                            self.show_two_board()
                            if self.ai.enemy_board.plus_shot():
                                print('AI попал в корабль! Дополнительный ход.')
                                continue
                            break
                    except ExitGame:
                        print('Выход из текущей игры')
                        input("Нажмите Enter для продолжения")
                        break
                    except DotOutBoard as e_1:
                        print(e_1)
                        print('повторите ввод')
                        self.show_two_board()
                        continue
                    except ShotDouble as e_2:
                        print(e_2)
                        print('повторите ввод')
                        self.show_two_board()
                        continue
            elif mode == '2':
                print('Генерирую новое расположение кораблей')
                continue
            elif mode == '0':
                print('Выход из программы')
                break

    def start(self):
        # print(self.greet())
        # self.user_board.random_board()
        # self.user_board.show_cont()
        # self.user_board.show_ships()
        # self.ai_board.random_board()
        # self.ai_board.show_cont()
        # self.ai_board.show_ships()
        # self.show_two_board()
        self.loop()
    
    def ask_mode(self):
        print("--------------------------------"*2)
        return input(" Выберите режим работы:   ")


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
# ggg.ai_board.show_cont()
ggg.ai_board.show_ships()
ggg.ai_board.shots.append(Dot(1, 1))
ggg.ai_board.shots.append(Dot(1, 2))
ggg.ai_board.show_shots()


ggg.show_two_board()
# %%
shhh = Ship(Dot(1, 1), 1, True)
shhh.dots()
# %%
ggg = Game()
# print(ggg.greet())
ggg.start()

# %%
