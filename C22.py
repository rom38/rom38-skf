# %%
class Square():
    def __init__(self, side):
        self.side = side


class SquareFactory():
    @staticmethod
    def side_square(side):
        return Square(side)


sq = SquareFactory.side_square(7)
print(sq)
print(sq.side)
# %%
# 2.3.4



