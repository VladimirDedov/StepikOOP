class Cell:
    def __init__(self, value: int = 0, is_free: bool = True):
        self.value = value
        self.is_free = is_free

    def __bool__(self):
        if self.value == 0:
            return True
        return False

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