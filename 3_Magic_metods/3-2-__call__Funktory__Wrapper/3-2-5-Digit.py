class DigitRetrieve:
    def __call__(self, num, *args, **kwargs):
        if self.is_int(num):
            return int(num)
        return None

    @staticmethod
    def is_int(str):
        try:
            int(str)
            return True
        except ValueError:
            return False


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
