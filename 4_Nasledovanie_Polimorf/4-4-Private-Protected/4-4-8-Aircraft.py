class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('неверный тип аргумента')

    def __verify_weight(self, weight):
        if type(weight) not in (int, float) or weight < 0:
            raise TypeError('неверный тип аргумента')

    def __setattr__(self, key, value):
        if key == '_model':
            self.__verify_name(value)
        elif key in ('_mass', '_speed', '_top'):
            self.__verify_weight(value)
        object.__setattr__(self, key, value)

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super(PassengerAircraft, self).__init__(model, mass, speed, top)
        if type(chairs) not in (int, ) or chairs < 0:
            raise TypeError('неверный тип аргумента')
        self._chairs=chairs



class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super(WarPlane, self).__init__(model, mass, speed, top)
        if type(weapons) not in (dict, ):
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]