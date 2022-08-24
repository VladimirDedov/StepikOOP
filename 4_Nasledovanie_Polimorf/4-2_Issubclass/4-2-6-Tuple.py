class Tuple(tuple):
    
    def __add__(self, other):
        return  Tuple(super(Tuple, self).__add__(tuple(other)))

t = Tuple([1, 2, 3])
print(t)
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)