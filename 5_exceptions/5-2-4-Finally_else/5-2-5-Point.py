class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

x,y=input().split()

try:
    pt=Point(int(x), int(y))
except ValueError:
    try:
        pt = Point(float(x), float(y))
    except:
        pt=Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")