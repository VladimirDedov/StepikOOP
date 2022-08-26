class SoftList(list):
    def __init__(self, lst):
        self.lst = list(lst)

    def __getitem__(self, item):
        try:
            return self.lst[item]
        except IndexError:
            return False
        
sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
print(sl[6])
sl[6] # False
sl[-7] # False