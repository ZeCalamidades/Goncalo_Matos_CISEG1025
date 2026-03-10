Marcas = []
Modelos = []

max_car = 100

#Funcoes

def int_dad():
    if len(Marcas) >= max_car:
        print("Máximo de dados na base de dados")
        return
    mar = input("Introduz a Marca: ")
    mod = input("Introduz o Modelo: ")

    for i in range(len(Marcas)):
        if mar == Marcas[i] and mod == Modelos[i]:
            print("Carro já existe na base de dados")
            return
        
    Marcas.append(mar)
    Modelos.append(mod)
    print("Veiculo Introduzido com sucesso!")        



def proc_dad():
    
    if len(Marcas) == 0:
        print("Não existem carros na base de dados!")
        return
    
    search = input ("Que modelo ou Marca procura: ")    

    for i in range(len(Marcas)):
        if search.lower() == Marcas[i].lower() or search.lower() == Modelos[i].lower():
            print(f"{i} | Marca: {Marcas[i]} | Modelos {Modelos[i]} ")
            return
        
    print("Veiculo não encontrado")
    repeat = input("Deseja procurar de novo (escreva sim para comfirmar): ")
    if repeat.lower() == "sim".lower:
        proc_dad()
    return

    
def eli_dad():

    if len(Marcas) == 0:
        print("Não existem carros na base de dados!")
        return

    for i in range(len(Marcas)):
        print(f"{i} | Marca: {Marcas[i]} | Modelo: {Modelos[i]}")

    try:
        delete = int(input("Qual o indice que deseja eliminar: "))
    except ValueError:
        print("Valor introduzido não é um indice")
        return

    if delete < 0 or delete >= len(Marcas):
        print("Indice inválido")
        return

    Marcas.pop(delete)
    Modelos.pop(delete)

    print("Veiculo eliminado com sucesso!")
#Menu

while True:
    print("\n------MENU------")
    print("1- Introduzir Dados")
    print("2- Procurar Dados")
    print("3- Eliminar Dados")
    print("4- Sair do Programa")
    
    opcao = input("Introduza o que pretende fazer: ")
    match opcao:
        case "1":
            int_dad()
        case "2":
            proc_dad()
        case "3":       
            eli_dad()
        case "4":
            print("Programa Terminado")
            break
        case _:
            print("Opção não reconhecida, tente de novo")    