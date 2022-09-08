TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        cls.__init__(args[0])

        if TYPE_OS ==1:
            return super().__new__(DialogWindows)
        else:
            return super().__new__(DialogLinux)