class Calendar:
    def __init__(self):
        self.__origin_user = ''
        self.__associates_taks = []
        self.__notes = {}  # {"id_notes":"obj"} |

class User:
    def __init__(self, user_name):
        self.__user_name = user_name
        self.__email = ''
        self.__password = ''

class SmallDataBase:
    def __init__(self, type_name):
        self.__database_type = type_name # settings, tasks, notes, mark's...
        self.__file = ""

''' Marca,
 pode ser de tarefas, notas, outras marcas(herança) e itens fixados, marca direta e indireta
    '''
class Mark:
    def __init__(self):
        self.id = id
        self.attributes = []

class Notes:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.text = ''
        self.creation_date = '' 
        self.markings = []
        # ↓titulo da nota parente↓
        self.parents = ''
        self.succession = "" 






class Tasks:  # sempre tem preferencia
    def __init__(self):
        self.id = ""
        self.titulo = ""
        self.description = []
        self.subtasks = []
        self.priority = []
        #
        self.valid_period = []
        self.invalid_period = []
        # notificação,alarme e layout específica (vem antes da categoria)
        self.notify = ""
        self.alarme = ""
        self.layout = ""
        #
        self.notes = [[],[],[],"","",""]   # uma secão ou pagina
        self.categories = []
        self.tags = []

