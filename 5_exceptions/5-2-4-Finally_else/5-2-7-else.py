def get_loss(w1, w2, w3, w4):
    try:
        y1=w1//w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        y = 10 * y1 - 5 * w2 * w3 + w4
        return y