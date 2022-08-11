class Player:
    def __init__(self, name: str, old: str, score: int):
        self.name = name
        self.old = old
        self.score = int(score)

    def __bool__(self):
        return self.score > 0


def get_list_word(st: str):
    lst = [i.strip() for i in st.split(';')]
    return lst


lst_in = [
    'Балакирев; 34; 2048',
    'Mediel; 27; 0',
    'Влад; 18; 9012',
    'Nina P; 33; 0'
]

players = []
for i in lst_in:
    players.append(Player(*get_list_word(i)))

iter = filter(bool, players)
players_filtered = [i for i in iter]
print(players_filtered, players, sep='\n')
