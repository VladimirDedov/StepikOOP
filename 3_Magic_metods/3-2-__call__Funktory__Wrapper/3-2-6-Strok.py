class RenderList:
    def __init__(self, type_list):
        self.__type_list=type_list

    def __call__(self, lst, *args, **kwargs):
        if self.__type_list=='ol':
            return self.get_string('ol', lst)
        else:
            return self.get_string('ul', lst)

    def get_string(self,teg, lst):
        result=f'<{teg}>'
        for s in lst:
            result+= f'<li>{s}</li>'
        result+=f'</{teg}>'
        return result


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)