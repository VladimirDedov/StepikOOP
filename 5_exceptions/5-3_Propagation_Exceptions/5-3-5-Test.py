class Test:
    def __init__(self, descr: str):
        if 10 <= len(descr) <= 10000:
            self._descr = descr
        else:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super(TestAnsDigit, self).__init__(descr)
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit <0:
            raise ValueError('недопустимые значения аргументов теста')
        self._ans_digit = ans_digit
        self._max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        if self._ans_digit - self._max_error_digit <= ans <= self._ans_digit + self._max_error_digit:
            return True
        return False
descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    test = TestAnsDigit(descr, ans)
    print(test.run())
except Exception as e:
    print(e)

try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False
