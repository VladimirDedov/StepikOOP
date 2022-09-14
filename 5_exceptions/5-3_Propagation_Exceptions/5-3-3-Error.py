def input_int_numbers():
    st=map(int,input().split())
    return tuple(st)

while True:
    try:
        c = input_int_numbers()
        break
    except:
        continue

print(*c)