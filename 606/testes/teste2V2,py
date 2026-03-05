Marcas = []
Modelos = []

max_carros = 100

#Funções

def Introduzir_dados():
    if len(Modelos) >= max_carros:
        print("Numero máximo de carros atingido")
        return
    
    Marca = input("Introduz a marca: ")
    Modelo = input("Introduz o modelo: ")

    for i in range(len(Marcas)):
        if Marca == Marcas[i] and Modelo == Modelos[i]:
            print("Carro já inserido!")
            return
    
    Marcas.append(Marca)
    Modelos.append(Modelo)
    print("Carro adicionado com sucesso!")        

def Procurar_dados():
    procura = input("Indique a marca ou o modelo que procure")
    encontrado = False

    for i in range(len(Marcas)):
        if (procura.lower in Marcas[i].lower() or 
            procura.lower in Modelos[i].lower()): 
            print(f"{i} | {Marcas[i]} | {Modelos[i]}")
            encontrado = True
    
    if not encontrado:
        print("Carro não encontrado")

def Eliminar_dados():
    if len(Marcas) == 0:
        print("Não existem Carros cadastrados.")
        return

    for i in range(len(Modelos)):
        print(f"Indice:{i} | Modelo:{Modelos[i]} | Marca:{Marcas[i]}")
    try:
        indice = int(input("Índice do Carro a excluir: "))
        if indice < 0 or indice >= len(Marcas):
            print("Índice inválido.")
            return

        confirmar = input("Tem a certeza que deseja excluir? (s/n)")
        if confirmar.lower() == "s":
            Marcas.pop(indice)
            Modelos.pop(indice)
            print("Carro excluído com sucesso.")
        else:
            print("Exclusão cancelada.")

    except ValueError:
        print("Entrada inválida. Use números.")

#Menu
while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Introduzir Dados")
    print("2 - Procurar Dados")
    print("3 - Eliminar Dados")
    print("4 - Sair do Programa")

    opcao = input("Escolha a opção: ")

    match opcao:
        case "1":
            Introduzir_dados()
        case "2":
            Procurar_dados()
        case "3":
            Eliminar_dados()
        case "4":
            print("Programa terminado.")
            break
        case _:
            print("Opção não reconhecida.")
