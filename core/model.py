
class Model:
    def __init__(self, *args, **kwargs):
        print("modelos de base")
        print(args)
        if 'mierda' in kwargs:
            print(kwargs['mierda'])