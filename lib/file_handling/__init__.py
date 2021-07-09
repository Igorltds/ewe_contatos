from lib.interface_basic import *

def exist(file_name):
    if not fileExist(file_name): create_file(file_name)

def fileExist(file_name):
    try: open(file_name, 'rt').close()
    except FileNotFoundError: return False
    else: return True

def create_file(file_name):
    try: open(file_name, "w+")
    except: print("Houve um erro na criação do arquivo")
    else: print(f"Arquivo {file_name} criado sucesso")


# leituras e registros
def read_users(file_name):
    try: file = open(file_name, "r")
    except: print(f"erro ao ler arquivo {file_name}")
    else:
        highlight("Usuarios Cadastradas", color_green())
        for linha in file:
            dado = linha.split(';')
            dado[0], dado[1] = dado[0].replace("\n",""), dado[1].replace("\n","")
            print(f"{dado[0]:<30} senha: {dado[1]:>3}")
    finally: input(color_yellow() + "\nEnter para prosseguir" + color_reset())

def read_contacts(file_name):
    try: file = open(file_name, "r")
    except: print(f"erro ao ler arquivo {file_name}")
    else:
        highlight("Pessoas Cadastradas", color_green())
        for linha in file:
            dado = linha.split(';')
            dado[0], dado[1] = dado[0].replace("\n",""), dado[1].replace("\n","")
            print(f"{dado[0]:<30} numero: {dado[1]:>3}")
    finally: input(color_yellow() + "\nEnter para prosseguir" + color_reset())

def register_user(file_name):
    highlight("Novo Cadastro de Usuário", color_blue())
    user_name = input_str("nome")
    password = get_password()
    if not fileExist(file_name): print("Houve um erro abertura do arquivo")
    else:
        try: open(file_name, "a").write(f'{user_name}; {password}\n')
        except: print("houve um erro na hora de escrever os dados! ")
        else: print(f"Sucesso no cadastro de {user_name}")

def register_contact(file_name):
    highlight("Novo Cadastro de Contato", color_blue())
    personal_name = input_str("nome")
    personal_nun = input_int("numero")
    if not fileExist(file_name): print("Houve um erro abertura do arquivo")
    else:
        try: open(file_name, "a").write(f'{personal_name}; {personal_nun}\n')
        except: print("houve um erro na hora de escrever os dados! ")
        else: print(f"Sucesso no cadastro de {personal_name}")
