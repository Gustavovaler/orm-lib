import mysql.connector
from ..default_settings import default_settings
from .errors import Error


class Connection :
    def __init__(self,**kwargs): 
        if 'user' in kwargs:
           self.user = kwargs['user']
        else:
            self.user = default_settings['user']

        if 'database' in kwargs:
            self.database = kwargs['database']
        else:            
            return Error.get_err('database')

        if 'host' in kwargs:
            self.host = kwargs['host']
        else:
            self.host = default_settings['host']

        if 'password' in kwargs:
            self.password = kwargs['password']
        else:
            self.password = default_settings['password']

        if 'port' in kwargs:
            self.port = kwargs['port']
        else: 
            self.port = default_settings['port']

        try:
            self.cnx = mysql.connector.connect(user=self.user,
                                             password=self.password,
                                             host=self.host,
                                             database=self.database,
                                             port=self.port) 
        except:
            return Error.unable_connect(user=self.user,
                                             password=self.password,
                                             host=self.host,
                                             database=self.database,
                                             port=self.port)



    def close(self):
        print("cerrando conexion")
        self.cnx.close()

    def cursor(self):
        self.cursor = self.cnx.cursor()
        return self.cursor



        


    