lst_in = input().split()
def validate(x):
     try:
         return int(x)
     except ValueError:
         try:
             return float(x)
         except:
             return x

lst_out=list(map(validate, lst_in))

print(lst_out)