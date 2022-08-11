class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        if len(args) == 0:
            self.lst_recipe = []
        else:
            self.lst_recipe = list(args)

    def add_ingredient(self, ing):
        self.lst_recipe.append(ing)

    def remove_ingredient(self, ing):
        self.lst_recipe.remove(ing)

    def get_ingredients(self):
        return tuple(self.lst_recipe)

    def __len__(self):
        return len(self.lst_recipe)


i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3
print(ings)
print(n)
