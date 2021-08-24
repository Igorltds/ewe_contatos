
''' #Programa Principal e teste
if False: #primeiro teste
    print("\n")
    ###
    if True: #criando Calendario
        calendario01 = Calendario()
        
    ###
    if True: #criando tag
        calendario01.criar_tag("0000000000000000", "para procastinar", "atividades para ocupar tempo que seria desperdiçado", ["id","id"])
        print(f"tag criada: {calendario01.tags[0].nome}")
    ###
    if True: #criando seção_notas
        calendario01.criar_secao_notas("0000000000000", "Estudos", "anotações relacionads com estudos", {"id":"obj"})
        print(f"seção de notas: {calendario01.secao_notas['0000000000000'].nome}")
    ###
    if True: #criando uma nota
        calendario01.criar_nota("0000000000000000", "idtag", "idcategoria", "fundamento matemático", "bládescriçãobla blá", "loremY_\nosdfasdfskjhksjhdfiwerh\nkjhdivuzldkjbqwkejhasfdm","secão id", "id nota", "id nota2")
        print(f"nota craiada: {calendario01.notas['0000000000000000'].titulo}")
    ###
    if True: #craindo categoria
        calendario01.criar_categoria("0000000000000000", "faculdade", {"0000000000000000": "obj", "0000000000000001": "obj2"}, [["id"], "id2"], {"id": "obj"}, {"blabla.img": "c:\\home"}, {"": ""}, {"": ""}, "config_not", "config_alarm", "config_layout", "medio")
        print(f"Categoria criada: {calendario01.categorias['0000000000000000'].nome}")
    ###
    if True: #criando tarefa
        calendario01.criar_tarefa("00000000000000", "titulo", "descricao", ["subtarefas"], "prioridade", {"periodo_valido":3030}, {"periodo_invalido":4040}, "notificacao_conf", "alarme_conf", "layout_conf", ["id","anotações",[]], "categoria_id", {"id":"obj"})
        print(f"Tarefa criada: {calendario01.tarefas['00000000000000'].titulo}")
    ###

    print("\n")
'''

''' base app
    def menu():
    x = 0
    while x >= 0:
        print("\n\n##----------------------------------------##"
              ,"\n   #Bem vindo ao esboço de calendario#"
              ,"\n##----------------------------------------##"
              ,"\n\n - Digite um numero negativo para fechar"
              ,"\n - Se não quiser coisa alguma digite 0"
              ,"\n - Se quiser logar digite 1"
              ,"\n - Se quiser criar calendario digite 2"
              ,"\n - Se quiser sair digite um numero negativo"
              ,"\n        ↓      ↓      ↓"
              ,"\n>>--------------------------")
        x = int(input("E o que vai ser? "))
        print("------------------------<<\n")

        if x == 1: #login
            login()
        if x == 2: #criação de calendario pessoal logon
            logon()
        if x < 0: #Fechar app
            resp = input("> Realmente quer sair do aplicativo? dados não salvos podem ser perdidos ('y' or 'n'): ")
            if resp == "y":
                pass
            else:
                x = 0
    def start(usuario, email, senha): #criar calendario
    calendario01 = Calendario(usuario, email, senha)
    print(f"Calendario criado, usuario: {calendario01.usuario}")
    def logon(): #crar usuario
    y = True
    while y: 
        usuario = input("digite um novo usario: ")
        email = input("digite um novo email: ")
        senha = input("digite uma nova senha: ")
        
        print("\n       -----------       ")
        start(usuario, email, senha)
        print("       -----------       \n")
        z = input("confirme para prosseguir")
        y = False
    def login(): #usar usuario
    pass

    menu()

'''