from math import sqrt

class PathLines:
    def __init__(self,*args):
        self.lst_line=[]
        self.lst_line.append(LineTo(0,0))
        for l in args:
            self.lst_line.append(l)

    def get_path(self):
        """возвращает список из объектов класса LineTo (если объектов нет, то пустой список);"""
        return self.lst_line

    def get_length(self):
        """возвращает суммарную длину пути (сумма длин всех линейных сегментов);"""
        res=0
        for i in range(1, len(self.lst_line)):
            res+=sqrt((self.lst_line[i].x - self.lst_line[i-1].x) ** 2 + (self.lst_line[i].y - self.lst_line[i-1].y) ** 2)
        return res
    def add_line(self, line):
        """добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута."""
        self.lst_line.append(line)
class LineTo:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y

# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
p = PathLines(LineTo(1, 2))
print(p.lst_line)
print(p.get_length())