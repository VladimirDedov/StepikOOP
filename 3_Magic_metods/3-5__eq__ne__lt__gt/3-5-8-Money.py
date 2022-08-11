class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def validate_cb(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        return True

    def __lt__(self, other):
        if self.validate_cb(other):
            return self.volume < round(other.volume * other.cb.rates['rub'], 1)

    def __eq__(self, other):
        if self.validate_cb(other):
            return self.volume == round(other.volume * other.cb.rates['rub'], 1)

    def __gt__(self, other):
        if self.validate_cb(other):
            return self.volume > round(other.volume * other.cb.rates['rub'], 1)


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def validate_cb(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        return True

    def __lt__(self, other):
        if self.validate_cb(other):
            if type(other) == MoneyR:
                return round(self.volume * self.cb.rates['rub'], 1) < other.volume
            else:
                return round(self.volume * self.cb.rates['rub'], 1) < round(other.volume * other.cb.rates['rub'], 1)

    def __eq__(self, other):
        if self.validate_cb(other):
            if type(other) == MoneyR:
                return round(self.volume * self.cb.rates['rub'], 1) == other.volume
            else:
                return round(self.volume * self.cb.rates['rub'], 1) == round(other.volume * other.cb.rates['rub'], 1)

    def __gt__(self, other):
        if self.validate_cb(other):
            if type(other) == MoneyR:
                return round(self.volume * self.cb.rates['rub'], 1) > other.volume
            else:
                return round(self.volume * self.cb.rates['rub'], 1) > round(other.volume * other.cb.rates['rub'], 1)


class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def validate_cb(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        return True

    def __lt__(self, other):
        if self.validate_cb(other):
            if type(other) == MoneyR:
                return round(self.volume * self.cb.rates['rub'], 1) < other.volume
            else:
                return round(self.volume * self.cb.rates['rub'], 1) < round(other.volume * other.cb.rates['rub'], 1)

    def __eq__(self, other):
        if self.validate_cb(other):
            if type(other) == MoneyR:
                return round(self.volume * self.cb.rates['rub'], 1) == other.volume
            else:
                return round(self.volume * self.cb.rates['rub'], 1) == round(other.volume * other.cb.rates['rub'], 1)

    def __gt__(self, other):
        if self.validate_cb(other):
            if type(other) == MoneyR:
                return round(self.volume * self.cb.rates['rub'], 1) > other.volume
            else:
                return round(self.volume * self.cb.rates['rub'], 1) > round(other.volume * other.cb.rates['rub'], 1)


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r < d:
    print("неплохо")
else:
    print("нужно поднажать")
