import random
from string import ascii_lowercase, digits
class EmailValidator:
    CHARS = "_." + ascii_lowercase+digits+ascii_lowercase.upper()


    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        len_email = email.split('@')
        chars = cls.CHARS + '@'
        if set(email)<=set(chars) and len(len_email[0])<=100 and len(len_email[1])<=50:
            if len_email[1].count('.') and not email.count('..'):
                return True
        return False

    @classmethod
    def get_random_email(cls):
        email=''
        lengh = random.randint(0,100)
        for i in range(lengh):
            email+=random.choice(cls.CHARS)
        email +='@gmail.com'
        return email

    @staticmethod
    def __is_email_str(email):
        return type(email) in (str,)
print(EmailValidator.CHARS)
print(EmailValidator.check_email('zx@.ry'))
res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)
res = EmailValidator.check_email("sc_lib@list..ru") # False
print(res)
res = EmailValidator.check_email("sc__lib@lis ") # False
print(res)
res = EmailValidator.check_email(".vu7PZS1VoSAWiqzoBHo8AedhnfhnfdoBHo8Aexw6HNTKOJOf@") # False
print(res)
