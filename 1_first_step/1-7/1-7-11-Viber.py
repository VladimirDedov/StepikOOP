class Viber:
    dct = []

    @classmethod
    def add_message(cls, msg):
        cls.dct.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.dct.remove(msg)


    def set_like(msg):
        indx = Viber.dct.index(msg)
        if Viber.dct[indx].fl_like:
            Viber.dct[indx].fl_like = False
        else:
            Viber.dct[indx].fl_like = True

    @classmethod
    def show_last_message(cls, numb):
        if numb>len(cls.dct):
            numb = len(cls.dct)
        for i in range(numb):
            print (cls.dct[i].text)
    @classmethod
    def total_messages(cls):
        return len(cls.dct)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.show_last_message(3)
Viber.remove_message(msg)
Viber.show_last_message(10)