class Body:
    def __init__(self,name: str, ro: 'number', volume:'number'):
        self.name = name
        self.ro=ro
        self.volume = volume

    def __lt__(self, other):
        if type(other) in (int,):
            return self.ro * self.volume < other
        else:
            return self.ro * self.volume < other.ro * other.volume

    def __eq__(self, other):
        if type(other) in (int,):
            return self.ro * self.volume == other
        else:
            return  self.ro*self.volume == other.ro*other.volume

    def __gt__(self, other):
        if type(other) in (int,):
            return self.ro * self.volume > other
        else:
            return  self.ro*self.volume > other.ro*other.volume
   # True, если масса тела body2 равна 5