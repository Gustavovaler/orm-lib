

class BaseRouter:
    """docstring for BaseRouter"""
    def __init__(self, arg):
        self.arg = arg

class Router(BaseRouter):
    """docstring for Router"""
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    @staticmethod
    def get(route, *args, **kwargs):
        print(route)
        if kwargs['controller']:
            print(kwargs['controller'])
        