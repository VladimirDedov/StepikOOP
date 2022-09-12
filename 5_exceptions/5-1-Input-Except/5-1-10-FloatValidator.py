class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value=min_value
        self.max_value=max_value

    def __call__(self, value):
        if type(value) not in (float,) or self.min_value > value or value > self.max_value:
            raise ValueError('значение не прошло валидацию')

class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value=min_value
        self.max_value=max_value

    def __call__(self, value):
        if type(value) not in (int,) or self.min_value > value or value > self.max_value:
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    fv, iv = validators
    lst_res=[]
    for ls in lst:
        try:
            t=fv(ls)
            lst_res.append(ls)
        except:
            try:
                t=iv(ls)
                lst_res.append(ls)
            except:
                pass
    return lst_res

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]

print(lst_out)