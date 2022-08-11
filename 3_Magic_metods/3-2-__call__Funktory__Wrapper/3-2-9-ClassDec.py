class InputDigits:
    def __init__(self, func):
        print('2')
        self.__fn = func
        print('4')

    def __call__(self, *args, **kwargs):
        print('3')
        st = self.__fn()
        lst_st = [int(i) for i in list(st.split(' '))]
        return lst_st


@InputDigits
def input_dg():
    print('1')
    res = input()
    return res

res = input_dg()

print(res)
