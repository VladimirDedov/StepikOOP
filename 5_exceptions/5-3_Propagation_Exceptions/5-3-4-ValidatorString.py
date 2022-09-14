class ValidatorString:
    def __init__(self, min_length, max_length, chars=''):
        self._min_length = min_length
        self._max_length = max_length
        self._chars = chars

    def is_valid(self, string):
        if type(string) != str or len(string) > self._max_length  or len(string) < self._min_length:
            raise ValueError('недопустимая строка')
        flag = True
        if self._chars:
            for i in self._chars:
                if i in string:
                    flag = False
                    break
            if flag:
                raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        self.login_validator.is_valid(request['login'])
        self.password_validator.is_valid(request['password'])
        self._login = request['login']
        self._password = request['password']


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
