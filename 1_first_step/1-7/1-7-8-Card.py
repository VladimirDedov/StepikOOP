from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits+'-'+' '
    @staticmethod
    def check_card_number(number):
        if len(number)!=19:
            return False
        for st in number:
            if st =="-" or st in digits:
                continue
            else:
                return False
        return True
    @classmethod
    def check_name(cls, name):
        if name.count(' ') > 1 or name.count(' ')==0:
            return False
        if set(name) <= set(cls.CHARS_FOR_NAME):
            return True
        else:
            return False

is_number = CardCheck.check_card_number("1234-5678-9022-1111")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)
print(is_name)