
class  BaseMigration
    """docstring for  BaseMigration"""
    def __init__(self):
        pass
        
class Migration(BaseMigration):
    """Migration base object"""    
    def __init__(self, arg):
        super().__init__()
        self.arg = arg
        