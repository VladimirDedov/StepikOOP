class Car:
    def __init__(self):
        self.__model=''
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) in (str,) and 2 <= len(model) <= 100:
            self.__model = model




car = Car()
car.model = "Toyota"
print(car.model)
car.model = "Moskvich"
print(car.model)
