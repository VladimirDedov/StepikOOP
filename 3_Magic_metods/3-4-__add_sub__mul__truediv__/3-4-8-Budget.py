class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money if isinstance(money, (int, float)) else 0

    def __add__(self, other):
        if type(other) == Item:
            return self.money + other.money
        return self.money + other

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self, budget_lst=None):
        self.budget_lst = budget_lst if budget_lst else []

    def add_item(self, it):
        self.budget_lst.append(it)

    def remove_item(self, indx):
        self.budget_lst.pop(indx)

    def get_items(self):
        return self.budget_lst


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
