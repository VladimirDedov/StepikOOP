import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:

    def init(self):
        count = 0
        while count < self.M:
            lst_i = []
            lst_j = []
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
            if i in lst_i and j in lst_j:
                continue
            self.pole[i][j].mine = True
            lst_i.append(i)
            lst_j.append(j)
            count += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    mines = sum(
                        (self.pole[x + i][y + j].mine for i, j in indx if 0 <= i + x < self.N and 0 <= j + y < self.N))
                    self.pole[x][y].around_mines = mines

    def __init__(self, N, M):
        self.M = M
        self.N = N
        self.pole = [[Cell() for j in range(N)] for i in range(N)]
        self.init()

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
a.show()
