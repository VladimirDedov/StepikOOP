class HandlerGet:
    def __init__(self, func):
        self.func=func

    def __call__(self,request, *args, **kwargs):
        m = request.get('method', 'GET')
        n = request.get('method', 'POST')
        if m == 'GET':
            return self.get(self.func, request)
        elif n == 'POST':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

