class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super(DetailView, self).__init__(methods)

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

        func=getattr(self, method.lower(), False)

        if func:
            return  func(request)


    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        for key in request:
            if key != 'url':
                raise TypeError('request не содержит обязательного ключа url')
        return f'url: {request["url"]}'

dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
