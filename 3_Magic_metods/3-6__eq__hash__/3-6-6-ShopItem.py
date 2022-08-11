class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

def get_list_word(st: str):
    name, right_st=st.split(':')
    weight, price=right_st.split()
    return [name, weight, price]

lst_in = [
    'Системный блок: 1500 75890.56',
    'Монитор Samsung: 2000 34000',
    'Клавиатура: 200.44 545',
    'Монитор Samsung: 2000 34000'
]
shop_items=dict()
total=1
for st in lst_in:
    st=get_list_word(st)
    obj=ShopItem(*st)
    for i in shop_items.keys():
        if hash(obj) == hash(i):
            shop_items[i]=[shop_items[i][0], shop_items[i][1]+1]
            break
    if obj not in shop_items:
        shop_items[obj]=[obj, total]

it1 = ShopItem('name', 10, 11)
it2 = ShopItem('Name', 10, 11)
print(hash(it1)==hash(it2))
for i in shop_items:
    print(shop_items[i][1])
