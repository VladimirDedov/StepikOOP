class Morph:
    def __init__(self, *words):
        self.words = list(words)

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return True if other.lower() in self.words else False


dict_words = [
    Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
    Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
          'формулах'),
    Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
          'векторами', 'векторах'),
    Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
          'эффектами', 'эффектах'),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
]
text = input()
count=0
for word_in_text in text.split(' '):
    for morph in dict_words:
        if word_in_text.strip('–?!,.;').lower() in morph.get_words():
            count+=1
            break

print(count)