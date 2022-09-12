x, y = input().split()

try:
    s=int(x)+int(y)
except ValueError:
    try:
        s = float(x) + float(y)
    except:
        s=x+y
finally:
    print(s)