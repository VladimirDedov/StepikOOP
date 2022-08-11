class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            lst_result = []
            st = func()
            for s in st.split():
                lst_result.append(self.__render(s))
            return lst_result
        return wrapper


class RenderDigit:
    def __call__(self, st, *args, **kwargs):
        try:
            return int(st)
        except ValueError:
            return None

render = RenderDigit()

@InputValues(render)
def input_dg():
    res = input()
    return res

res = input_dg()
print(res)
