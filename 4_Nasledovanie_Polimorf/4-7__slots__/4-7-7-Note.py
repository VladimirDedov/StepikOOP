class Note:
    def __init__(self, name, ton):
        self._name=name
        self._ton=ton

    def __setattr__(self, key, value):
        if key=='_name':
            if value not in ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']:
                raise ValueError('недопустимое значение аргумента')
        elif key== '_ton':
            if value not in (-1, 0, 1):
                raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)

class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    notes_lst = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'
    __flag = None

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __new__(cls, *args, **kwargs):
        if cls.__flag is None:
            cls.__flag = super().__new__(cls, *args, **kwargs)
        return cls.__flag

    def __getitem__(self, item):
        if not(0<=item < 7) or type(item) != int:
            raise IndexError('недопустимый индекс')

        if item ==0:
            return self._do
        elif item ==1:
            return self._re
        elif item == 2:
            return self._mi
        elif item ==3:
            return self._fa
        elif item == 4:
            return self._solt
        elif item ==5:
            return self._la
        elif item == 6:
            return self._si

    def __setitem__(self, key, value):
        self.__slots__[key]= value


notes = Notes()

# print(notes[2], notes._mi)
# nota = notes[2]  # ссылка на ноту ми
notes[2]._ton = -1 # изменение тональности ноты фа

print(notes[2]._ton)
print(notes.__dir__)
