# =========================
# FUNÇÕES PARA OS NÚMEROS
# =========================

def ler_numero():
    while True:
        try:
            n = int(input("Introduza um número entre 1 e 1000: "))
            if 1 <= n <= 1000:
                return n
            else:
                print("Número fora do intervalo.")
        except ValueError:
            print("Erro: introduza um número inteiro válido.")


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def contar_divisores(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n


def par_ou_impar(n):
    return "Par" if n % 2 == 0 else "Ímpar"


def menu_numeros():
    total = 0

    while total < 100:
        for _ in range(10):
            if total >= 100:
                break

            numero = ler_numero()
            total += 1

            print("\nNúmero:", numero)
            print("Primo:", "Sim" if eh_primo(numero) else "Não")
            print("Divisores:", contar_divisores(numero))
            print("Perfeito:", "Sim" if eh_perfeito(numero) else "Não")
            print("Paridade:", par_ou_impar(numero))

        if total < 100:
            op = input("\nDeseja continuar? (s/n): ").lower()
            if op == "n":
                break
# =========================
# FUNÇÕES DO CATÁLOGO
# =========================

def livro_existe(titulo, autor, titulos, autores):
    for i in range(len(titulos)):
        if titulo == titulos[i] and autor == autores[i]:
            return True
    return False


def adicionar_livro(titulos, autores, anos):
    if len(titulos) >= 100:
        print("Limite de livros atingido.")
        return

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")

    if livro_existe(titulo, autor, titulos, autores):
        print("Livro já cadastrado.")
    else:
        titulos.append(titulo)
        autores.append(autor)
        anos.append(ano)
        print("Livro adicionado com sucesso.")


def procurar_livro(titulos, autores, anos):
    termo = input("Introduza título ou autor: ")
    encontrado = False

    for i in range(len(titulos)):
        if termo.lower() in titulos[i].lower() or termo.lower() in autores[i].lower():
            print(f"{i} | {titulos[i]} | {autores[i]} | {anos[i]}")
            encontrado = True

    if not encontrado:
        print("Nenhum livro encontrado.")


def excluir_livro(titulos, autores, anos):
    try:
        for i in range(len(titulos)):
            print(f"{i} | {titulos[i]} | {autores[i]} | {anos[i]}")

        indice = int(input("Índice do livro a excluir: "))

        if indice in range(len(titulos)):
            titulos.pop(indice)
            autores.pop(indice)
            anos.pop(indice)
            print("Livro removido com sucesso.")
        else:
            print("Índice inválido.")

    except ValueError:
        print("Erro: introduza um número válido.")


def ordenar_livros(titulos, autores, anos):
    print("1 - Ordenar por Título")
    print("2 - Ordenar por Autor")
    opc = input("Escolha: ")

    if opc == "1":
        ordem = sorted(range(len(titulos)), key=lambda i: titulos[i].lower())
    elif opc == "2":
        ordem = sorted(range(len(autores)), key=lambda i: autores[i].lower())
    else:
        print("Opção inválida.")
        return

    titulos[:] = [titulos[i] for i in ordem]
    autores[:] = [autores[i] for i in ordem]
    anos[:] = [anos[i] for i in ordem]

    print("Livros ordenados com sucesso.")


def listar_livros(titulos, autores, anos):
    if len(titulos) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for i in range(len(titulos)):
            print(f"{i} | {titulos[i]} | {autores[i]} | {anos[i]}")
# =========================
# PROGRAMA PRINCIPAL
# =========================

titulos = []
autores = []
anos = []

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Ver números")
    print("2 - Catálogo de livros")
    print("3 - Sair do Programa")

    escolha = input("Escolha a opção: ")

    match escolha:
        case "1":
            menu_numeros()

        case "2":
            while True:
                print("\n--- CATÁLOGO DE LIVROS ---")
                print("1 - Adicionar novo livro")
                print("2 - Procurar por título ou autor")
                print("3 - Excluir livro")
                print("4 - Ordenar livros")
                print("5 - Listar livros")
                print("6 - Voltar ao menu principal")

                opc = input("Escolha: ")

                match opc:
                    case "1":
                        adicionar_livro(titulos, autores, anos)
                    case "2":
                        procurar_livro(titulos, autores, anos)
                    case "3":
                        excluir_livro(titulos, autores, anos)
                    case "4":
                        ordenar_livros(titulos, autores, anos)
                    case "5":
                        listar_livros(titulos, autores, anos)
                    case "6":
                        break
                    case _:
                        print("Opção inválida.")

        case "3":
            print("Programa terminado.")
            break

        case _:
            print("Opção inválida.")
