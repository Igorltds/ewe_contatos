from interface_main import *
from classes import *

def beginning():
    print_spotlight('Calender', 40)
    new = check_file()
    if new:
        gen_user(input("Seu nome de usuario: "))
    
def gen_user(user_name):
    User(user_name)
    

def check_file():
    try:
        open("date_main.txt","r")
    except FileNotFoundError:
        print("arquivo não existe, criando um novo")
        open("date_main.txt", "w")
        return True
    else:
        return False


beginning()
 