lst_in = input().split()

def validate(x):
    try:
        int(x)
        return True
    except:
        return False

lst_int=sum(map(int,filter(validate, lst_in)))
print(lst_int)