from ..default_settings import default_settings

class BaseError:
    def __init__(self):
        self.error = 'Error'

class Error(BaseError):
    def __init__(self, *args, **kwargs):
        super().__init__()

    @staticmethod
    def get_err(code):
        if code == 'database':
            print('**************')
            print('No se asignó ninguna base de datos')
            print('**************')
            return exit()

    @staticmethod
    def unable_connect(*args, **kwargs):

        print('''***************************************************
           \r No se pudo establecer conexión con la base de datos\r
           \r Es posible que el  puerto que haya configurado esté siendo
            \r usado por otra aplicación.
            \r********************************************************
            ''')
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                print(k,' : ' ,v)


               
        

        return exit()
