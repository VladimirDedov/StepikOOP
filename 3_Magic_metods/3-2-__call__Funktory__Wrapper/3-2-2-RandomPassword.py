import random



class RandomPassword :
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars=psw_chars
        self.min_length=min_length
        self.max_length=max_length

    def __call__(self, *args, **kwargs):
        password =''
        count = random.randint(self.min_length, self.max_length)
        for i in range(count):
            password += random.choice(self.psw_chars)
        return password
p=RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [p() for i in range(3)]

ran=p()
print(lst_pass)