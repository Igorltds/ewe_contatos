# formatação visual #
def line(tam=42):
    return "-" * tam
def highlight(txt, color="", tam=42):
    print(f"\n#{'-'*tam}#\n {(color + txt + color_reset()).center(tam)}\n#{'-'*tam}#")
# formatação visual #
''''''
# cores #
def color_reset():
    return "\033[0;0m"
def color_red():
    return "\033[31m"
def color_green():
    return "\033[32m"
def color_yellow():
    return "\033[33m"
def color_blue():
    return "\033[34m"
# cores #
''''''
# funções reutilizaveis #
def selection_of_options(list):
    x = 0
    print("Selecione uma dessas opções: \n")
    for item in list:
        x += 1
        print(f"{color_blue()}{x}{color_reset()} - {item}.")        
def input_int(variable_name):
    while True:
        try:
            nun_int = int(
                input(f"\ndigite um valor de {variable_name}:{color_green()}"))
        except:
            print(color_reset())
            input_error(", um numero inteiro")
        else:
            print(color_reset())
            return nun_int
def input_str(variable_name):
    while True:
        try:
            txt_str = input(f"Digite um {variable_name}: {color_green()}")

        except:
            print(color_reset())
            input_error()
        else: 
            print(color_reset())
            for x in txt_str.split(" "):
                if not x.isalpha():
                    input_error(", apenas nomes")
                else:
                    return txt_str
def get_password():
    while True:
        try:
            user_key = input(f"\nDigite uma senha:{color_green()}")
        except:
            print(color_reset())
            input_error(" como se tá bugando uma string?? ")
        else:
            print(color_reset())
            return user_key
def input_error(adtional = ""):
    print(line(10).center(30))
    print(f"{color_red()}Erro{color_reset()} digite algo valido{adtional}".center(42))
    print(line(10).center(30))
def leave():
    while True:
        try: answer = input(f"certeza que quer {color_red()}sair{color_reset()}? ({color_red()}S{color_reset()}/{color_red()}N{color_reset()}): ")
        except: input_error(f"(digite 's' ou 'n')")
        else:
            if answer == 's' or answer == 'S': highlight("Byee :)", color_yellow()), exit() 
            elif answer == "n" or answer == "N": return 
            else: input_error(f"(digite 's' ou 'n')")
# funções reutilizaveis #
''''''
