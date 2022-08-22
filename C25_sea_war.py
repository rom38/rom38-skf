# %%
class BoardExeption(Exception):
    pass


class Dot():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, alt_dot: 'Dot'):
        if not isinstance(alt_dot, Dot):
            raise ValueError("Передано неправильное значение")
            # return False
        if self.x == alt_dot.x and self.y == alt_dot.y:
            return True
        return False

    def near(self):
        dots_near: list = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
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


class Board():
    ships: list[Ship]
    hid: bool
    live_ships: int

    def __init__(self):
        self.map_br = []
        for y in range(6):
            self.map_br.append([])
            for x in range(6):
                self.map_br[y].append("O")

    def add_ship(self):
        pass

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
        return map_vis[:-1].split('\n')

        # hid: bool
        pass

    def out(self) -> bool:
        # exeption out, retry
        return True

    def shot(self):
        pass


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
    pass


class Game():
    user: User
    user_board: Board
    ai: AI
    ai_board: Board

    def __init__(self) -> None:
        self.user_board = Board()
        self.ai_board = Board()

    def show_two_board(self):
        for y1, y2 in zip(self.user_board.show(),
                          self.ai_board.show()):
            print(f"{y1}       {y2}")

    def random_board(self):
        pass

    def greet(self) -> str:
        return "greet"

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
ggg.show_two_board()
# %%
