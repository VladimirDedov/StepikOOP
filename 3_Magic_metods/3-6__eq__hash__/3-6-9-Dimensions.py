class Dimensions:
    def __init__(self, a, b, c):
        self.a =a
        self.b=b
        self.c=c
    def __setattr__(self, key, value):
        if value <=0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            return object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

def get_list_word(st: str):
    lst = []
    lst_temp = []
    for count in st.split(';'):
        for i in count.split():
            try:
                lst_temp.append(int(i))
            except:
                lst_temp.append(float(i))
        lst.append(lst_temp[:])
        lst_temp.clear()
    return lst


s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
lst_numb=get_list_word(s_inp)
lst_dims=[Dimensions(*lst) for lst in lst_numb]
dict_hash={hash(key) : key for key in lst_dims}
lst_sort_hash = sorted(dict_hash)
lst_dims=[dict_hash[key] for key in lst_sort_hash]

print(lst_sort_hash)


print(lst_dims)