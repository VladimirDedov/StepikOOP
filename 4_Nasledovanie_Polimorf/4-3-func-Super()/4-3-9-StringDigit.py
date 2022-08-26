class StringDigit(str):
    def __init__(self, string):
        self.validate(string)
        self.string = string

    @staticmethod
    def validate(string):
        for st in string:
            try:
                int(st)
            except ValueError:
                raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return StringDigit(self.string + other)

    def __radd__(self, other):
        return StringDigit(other + self.string)


sd = StringDigit("123")
print(type(sd))
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = sd + "789"  # StringDigit: 789123456
print(type(sd))
sd = sd + "f"  # ValueError
print(sd)
