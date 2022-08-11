class StringText:
    def __init__(self, lst=None):
        self.lst_words = lst if type(lst) == list else []

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __len__(self):
        return len(self.lst_words)


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]
lst_word_stich = []
for st in stich:
    lst = st.split(' ')
    lst = [lst[i].strip('–?!,.;') for i in range(len(lst)) if lst[i].strip('–?!,.;') != '']
    lst_word_stich.append(lst)

lst_text = []
for lst_words in lst_word_stich:
    lst_text.append(StringText(lst_words))

lst_text_sorted = lst_text[:]
lst_text_sorted = sorted(lst_text_sorted, key=lambda x: len(x), reverse=True)

res = []
for st in lst_text_sorted:
    res.append(' '.join(st.lst_words))
lst_text_sorted=res

