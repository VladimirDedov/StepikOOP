class Model:
    flag = True
    def query(self, **kwargs):
        self.dict=kwargs
        Model.flag = False


    def __str__(self):
        if Model.flag:
            return 'Model'
        else:
            text='Model: '
            for key, value in self.dict.items():
                text+=f'{key} = {value}, '
            return text[:-2]

model = Model()
#model.query(id = 1, fio = 'Sergey', old = 33)
print(model)