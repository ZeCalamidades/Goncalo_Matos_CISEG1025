Title = []
Director = []
Year = []
Genre = []

max_filmes = 100
ano_atual = 2026
skip = ""

def insert_movie():
    if len(Title) >= max_filmes:
        print("Base de dados está cheia")
        return
    tit = input("Coloca o titulo do filme: ")
    dir = input("Coloca o diretor do filme: ")
    genero = input("Coloca o genero do filme: ")
    
    try:
        ano = int(input("Coloca o ano do filme: "))
        if ano < 1888 or ano > ano_atual:
            print("Ano inválido")
            return   
    except ValueError:
        print("Ano tem de ser um valor numérico")        
        return
    for i in range(len(Title)):
        if tit.lower() == Title[i].lower() and dir.lower() == Director[i].lower():
            print("Filme já introduzido na base de dados")
            return
    Title.append(tit)
    Director.append(dir)
    Year.append(ano)
    Genre.append(genero)
    print("Filme introduzido com sucesso")

def search_movie():
    if len(Title) == 0:
        print("Não existem filmes na base de dados")
        return 

    search = input("Introduza o titulo, o diretor ou o genero do filme: ")
    found = False

    for i in range(len(Title)):
        if search.lower() == Title[i].lower() or search.lower() == Director[i].lower() or search.lower() == Genre[i].lower():
            print(f"{i} | Titulo {Title[i]} | Diretor {Director[i]} | Ano {Year[i]} | Genero {Genre[i]}")
            found = True

    if not found:
        print("Filme não encontrado")        

def delete_movie():
    if len(Title) == 0:
        print("Não existem filmes na base de dados")
        return    
    for i in range(len(Title)):
        print(f"{i} | Titulo {Title[i]} | Ano {Year[i]} | Genero {Genre[i]}")
    try:
        apagar = int(input("Introduza o indice do filme que pretende apagar: "))    
        if apagar >= 0 and apagar < len(Title):
            confirm = input(f"Comfirma que quer apagar o filme {Title[apagar]}? (s/n): ")
            while confirm.lower() not in ["s","n","sim","nao"]:
                print("Opção Inválida")
                confirm = input(f"Confirma que quer apagar o filme {Title[apagar]}? (s/n): ")
            if confirm.lower() == "s".lower() or confirm.lower() == "sim".lower():
                Title.pop(apagar)
                Director.pop(apagar)
                Year.pop(apagar)
                Genre.pop(apagar)
                print("Filme Apagado com sucesso!")
                return
            else:
                print("Voltando ao Menu")
                return
        else:
            print("Indice não é válido")    
            return
    except ValueError:
        print("Indice indicado não é um numero valido")
        return
    
def order_movie():
    if len(Title) == 0:
        print("Não existem filmes na base de dados")
        return
    print("1 - Ordenar por Titulo")
    print("2 - Ordenar por Diretor")
    print("3 - Ordenar por Ano de lançamento")
    print("4 - Voltar ao Menu")
    order = input("Escolha a opção que deseja executar: ")

    match order:
        
        case "1":
            ordem = sorted(range(len(Title)), key=lambda i: Title[i].lower())
        case "2":
            ordem = sorted(range(len(Director)), key=lambda i: Director[i].lower())
        case "3":
            ordem = sorted(range(len(Year)), key=lambda i: Year[i])
        case "4":
            print("Voltando ao Menu")
            return
        case _:
            print("Opção não reconhecida, tente de novo: ")
            order_movie()
    
    novo_titulos   = [Title[i] for i in ordem]
    novo_diretores = [Director[i] for i in ordem]
    novo_anos      = [Year[i] for i in ordem]
    novo_generos   = [Genre[i] for i in ordem]

    Title[:]   = novo_titulos
    Director[:] = novo_diretores
    Year[:]      = novo_anos
    Genre[:]   = novo_generos

    print("Filmes ordenados com sucesso.")

def list_movie():
    if len(Title) == 0:
        print("Não existem filmes na base de dados")
        return    
    for i in range(len(Title)):
        print(f"{i} | Titulo {Title[i]} | Ano {Year[i]} | Genero {Genre[i]}")
        skip = input("Carregue num botão para voltar ao menu: ")
        if skip != "":
            return

while True:
    print("\n-----MENU-----")
    print("1 - Inserir Filme")
    print("2 - Procurar Filme")
    print("3 - Excluir Filme")
    print("4 - Ordenar Filmes")
    print("5 - Listar Filmes")
    print("6 - Sair do Programa")
    opc = input("Introduza a opção que deseja realizar: ")
    
    match opc:

        case "1":
            insert_movie()
        
        case "2":
            search_movie()
        
        case "3":    
            delete_movie()

        case "4":
            order_movie()
        
        case "5":           
            list_movie()
        
        case "6":
            print("Progama Encerrado")
            break
        case _:
            print("Opção não reconhecida")