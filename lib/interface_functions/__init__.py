from lib.interface_basic import *
from lib.file_handling import *

def home_menu():
    while True:
        highlight("Bem vindo :)", color_green())
        selection_of_options(["usuarios","contatos", "", "sair do sistema" ])
        answer = input_int("menu")
        if answer == 1: users_menu()
        elif answer == 2: contacts_menu()
        elif answer == 3: break
        elif answer == 4: leave()
        else: input_error()

def users_menu():
    while True:
        highlight("Menu de Usuarios", color_blue())
        selection_of_options(["Exibir Usuarios","Cadastrar novo Usuario","Voltar", "Sair do sistema"])
        answer = input_int("menu")
        if answer == 1: read_users("date_users.txt")
        elif answer == 2: register_user("date_users.txt")
        elif answer == 3: home_menu()
        elif answer == 4: leave()
        else: input_error()

def contacts_menu():
    while True:
        highlight("Menu de Contatos", color_blue())
        selection_of_options(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Voltar", "Sair do Sistema"])
        answer = input_int("menu")
        if answer == 1: read_contacts("date_contacts.txt")
        elif answer == 2: register_contact("date_contacts.txt")
        elif answer == 3: home_menu()
        elif answer == 4: leave()
        else: input_error()
def leave():
    while True:
        try: answer = input(f"certeza que quer {color_red()}sair{color_reset()}? ({color_red()}S{color_reset()}/{color_red()}N{color_reset()}): ")
        except: input_error(f"(digite 's' ou 'n')")
        else:
            if answer == 's' or answer == 'S': clear(), "\n\n\n", highlight("Byee :)", color_yellow()), clear(3,0), quit()
            elif answer == "n" or answer == "N": return 
            else: clear(), input_error(f"(digite 's' ou 'n')")
            