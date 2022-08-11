class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width=None
        self.__height=None
        self.width = width
        self.height = height

    def show(self):
        print(f'{self.__title}:{self.__width},{self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if self.valid(val):

            self.__width = val
            if self.__width:
                self.show()


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if self.valid(val):

            self.__height = val
            if self.__height:
                self.show()


    @staticmethod
    def valid(val):
        return type(val) == int and 0 <= val <= 10000


a = WindowDlg('name', 10, 20)
a.width = 10.2
a.height = 0
a.width = 15
a.height = 0.5

print(a.width, a.height)
