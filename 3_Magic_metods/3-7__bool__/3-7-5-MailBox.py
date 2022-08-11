class MailBox:
    def __init__(self):
        self.inbox_list = []

    def get_list_word(self, st: str):
        lst = [i.strip() for i in st.split(';')]
        return lst

    def receive(self):
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                  'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                  'Python ООП; Балакирев С.М.; 2022',
                  'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        for i in lst_in:
            self.inbox_list.append(MailItem(*self.get_list_word(i)))

        self.inbox_list[0].set_read(True)
        self.inbox_list[-1].set_read(True)

class MailItem:
    def __init__(self, mail_from: str, title: str, content: str):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read=fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
inbox_list_filtered=list(filter(bool, mail.inbox_list))
print(inbox_list_filtered)
