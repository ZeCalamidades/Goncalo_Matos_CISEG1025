titulos = []
diretores = []
anos = []
generos = []

MAX_FILMES = 100
ANO_ATUAL = 2026


def adicionar_filme():
    if len(titulos) >= MAX_FILMES:
        print("Limite de 100 filmes atingido.")
        return

    titulo = input("Título: ")
    diretor = input("Diretor: ")
    genero = input("Gênero: ")

    try:
        ano = int(input("Ano de lançamento: "))
        if ano < 1888 or ano > ANO_ATUAL:
            print("Ano inválido. Deve estar entre 1888 e 2026.")
            return
    except ValueError:
        print("Ano deve ser um número inteiro.")
        return
    for i in range(len(titulos)):
        if titulo == titulos[i] and diretor == diretores[i]:
            print("Filme já cadastrado.")
            return

    titulos.append(titulo)
    diretores.append(diretor)
    anos.append(ano)
    generos.append(genero)
    print("Filme adicionado com sucesso.")


def procurar_filme():
    procura = input("Procurar por título, diretor ou gênero: ")
    encontrado = False

    for i in range(len(titulos)):
        if (procura.lower() in titulos[i].lower() or
            procura.lower() in diretores[i].lower() or
            procura.lower() in generos[i].lower()):
            print(f"{i} | {titulos[i]} | {diretores[i]} | {anos[i]} | {generos[i]}")
            encontrado = True

    if not encontrado:
        print("Nenhum filme encontrado.")


def excluir_filme():
    listar_filmes()

    try:
        indice = int(input("Índice do filme a excluir: "))
        if indice < 0 or indice >= len(titulos):
            print("Índice inválido.")
            return

        confirmar = input("Tem a certeza que deseja excluir? (s/n): ")
        if confirmar.lower() == "s":
            titulos.pop(indice)
            diretores.pop(indice)
            anos.pop(indice)
            generos.pop(indice)
            print("Filme excluído com sucesso.")
        else:
            print("Exclusão cancelada.")

    except ValueError:
        print("Entrada inválida. Use números.")


def ordenar_filmes():
    print("1 - Ordenar por Título")
    print("2 - Ordenar por Diretor")
    print("3 - Ordenar por Ano")

    opcao = input("Escolha: ")

    if opcao == "1":
        ordem = sorted(range(len(titulos)), key=lambda i: titulos[i].lower())
    elif opcao == "2":
        ordem = sorted(range(len(diretores)), key=lambda i: diretores[i].lower())
    elif opcao == "3":
        ordem = sorted(range(len(anos)), key=lambda i: anos[i])
    else:
        print("Opção inválida.")
        return

    novo_titulos   = [titulos[i] for i in ordem]
    novo_diretores = [diretores[i] for i in ordem]
    novo_anos      = [anos[i] for i in ordem]
    novo_generos   = [generos[i] for i in ordem]

    titulos[:]   = novo_titulos
    diretores[:] = novo_diretores
    anos[:]      = novo_anos
    generos[:]   = novo_generos

    print("Filmes ordenados com sucesso.")



def listar_filmes():
    if len(titulos) == 0:
        print("Não existem filmes cadastrados.")
        return

    for i in range(len(titulos)):
        print(f"{i} | {titulos[i]} | {diretores[i]} | {anos[i]} | {generos[i]}")
        print("-" * 50)


while True:
    print("\n----- Catálogo de Filmes -----")
    print("1 - Adicionar novo filme")
    print("2 - Procurar filme")
    print("3 - Excluir filme")
    print("4 - Ordenar filmes")
    print("5 - Listar filmes")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            adicionar_filme()
        case "2":
            procurar_filme()
        case "3":
            excluir_filme()
        case "4":
            ordenar_filmes()
        case "5":
            listar_filmes()
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("Opção não reconhecida.")
