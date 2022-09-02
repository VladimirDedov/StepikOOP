from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self._size = 3
        self._win = 0
        self.pole = tuple(tuple(Cell() for _ in range(self._size)) for _ in range(self._size))

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if not (0 <= r < self._size) or not (0 <= c < self._size):
            raise IndexError('некорректно указанные индексы')
        return r, c

    def __getitem__(self, item):
        r, c = self.__check_index(item)
        return self.pole[r][c].value

    def __update_win_status(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return
        for i in range(self._size):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self._size)):
            self._win = 1
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self._size)):
            self._win = 2
            return
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self._win = 3
            return

    def __setitem__(self, key, value):  # Если что, ошибка здесь
        r, c = self.__check_index(key)
        self.pole[r][c].value = value
        self.__update_win_status()

    def init(self):
        for i in range(self._size):
            for j in range(self._size):
                self.pole[i][j].value = 0
        self._win = 0

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if x.value == 0 else x.value, row))
        print('******************************************')

    def human_go(self):
        if not self:
            return

        while True:
            i, j = map(int, input('input coords: ').split())
            if not (0 <= i < self._size) or not (0 <= j < self._size):
                continue
            if self[i,j] == self.FREE_CELL:
                self[i,j] = self.HUMAN_X
                break

    def computer_go(self):
        if not self:
            return

        while True:
            i = randint(0, self._size - 1)
            j = randint(0, self._size - 1)
            if not (0 <= i < self._size) or not (0 <= j < self._size):
                continue
            if self[i,j] == self.FREE_CELL:
                self[i,j] = self.COMPUTER_O
                break

    @property
    def is_human_win(self):
        return self._win == 1

    @property
    def is_computer_win(self):
        return self._win == 2

    @property
    def is_draw(self):
        return self._win == 3

    def __bool__(self):
        return self._win == 0 and self._win not in (1,2,3)

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")