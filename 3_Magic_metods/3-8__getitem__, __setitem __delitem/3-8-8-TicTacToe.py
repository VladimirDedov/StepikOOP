class TicTacToe:
    def create_pole(self):
        tmp_list = []
        list_to_tuple = []
        for i in range(3):
            for j in range(3):
                tmp_list.append(Cell())
            list_to_tuple.append(tuple(tmp_list))
            tmp_list.clear()
        return tuple(list_to_tuple)

    def __init__(self):
        self.pole = self.create_pole()

    def __getitem__(self, item):
        i, j = item
        if type(i) == slice:
            return tuple(self.pole[x][j].value for x in range(3))
        elif type(j) == slice:
            return tuple(self.pole[i][x].value for x in range(3))
        self.validate(item)
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.validate(key)
        i, j = key
        if self.pole[i][j].is_free:
            self.pole[i][j].value = value
            self.pole[i][j].is_free=False
        else:
            raise ValueError('клетка уже занята')

    def validate(self, indx):
        if type(indx) !=slice:
            i,j = indx
            if i < 0 or i > 2 or j < 0 or j > 2:
                raise IndexError('неверный индекс клетки')

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value=0
                self.pole[i][j].is_free=True


class Cell:
    def __init__(self, value: int = 0, is_free: bool = True):
        self.value = value
        self.is_free = is_free

    def __bool__(self):
        if self.value == 0:
            return True
        return False


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
print(game.pole[0][0].is_free)
#game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
game.clear()
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print(v1)