from lib.front_basic import *
from lib.file_handling import *

def home_menu(data_users, data_contacts):
    while True:
        highlight("Bem vindo :)", color_green())
        selection_of_options(["usuarios","contatos", "", "sair do sistema" ])
        answer = input_int("menu")
        if answer == 1: users_menu(data_users)
        elif answer == 2: contacts_menu(data_contacts)
        elif answer == 3: pass
        elif answer == 4: leave()
        else: input_error()

def users_menu(data_users):
    while True:
        highlight("Menu de Usuarios", color_blue())
        selection_of_options(["Exibir Usuarios","Cadastrar novo Usuario","Voltar", "Sair do sistema"])
        answer = input_int("menu")
        if answer == 1: 
            highlight("Usuarios Cadastradas", color_green())
            for x in read_users(data_users):
                for y in x:
                    print(y)
            input(color_yellow() + "\nEnter para prosseguir" + color_reset())

        elif answer == 2: 
            highlight("Novo Cadastro de Usuário", color_blue())
            user_name = input_str("nome")
            password = get_password()
            register_user(data_users, user_name, password)
        elif answer == 3: home_menu()
        elif answer == 4: leave()
        else: input_error()

def contacts_menu(data_contacts):
    while True:
        highlight("Menu de Contatos", color_blue())
        selection_of_options(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Voltar", "Sair do Sistema"])
        answer = input_int("menu")
        if answer == 1: read_contacts(data_contacts)
        elif answer == 2: register_contact(data_contacts)
        elif answer == 3: home_menu()
        elif answer == 4: leave()
        else: input_error()
def leave():
    while True:
        try: answer = input(f"certeza que quer {color_red()}sair{color_reset()}? ({color_red()}S{color_reset()}/{color_red()}N{color_reset()}): ")
        except: input_error(f"(digite 's' ou 'n')")
        else:
            if answer == 's' or answer == 'S': clear(), highlight("Byee :)", color_yellow()), clear(1,0), quit()
            elif answer == "n" or answer == "N": return 
            else: clear(), input_error(f"(digite 's' ou 'n')")

            
