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
        
    def __repr__(self) -> str:
        return f'Dot(x={self.x}, y={self.y})'


class Ship():
    len_sh: int = 0
    nos: Dot
    vrt_hrz: bool
    life: int

    def dots(self):
        pass


class Board():
    map_br: list[list] = []
    ships: list[Ship]
    hid: bool
    live_ships: int

    def __init__(self):
        for i in range(6):
            self.map_br.append([])
            for j in range(6):
                self.map_br[i].append(Dot(j, i))


    def add_ship(self):
        pass

    def contour(self):
        pass

    def show(self):
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
print(xxx.map_br)
# %%
