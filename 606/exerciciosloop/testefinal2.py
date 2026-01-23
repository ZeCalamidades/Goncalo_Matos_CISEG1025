NumCli = []
NomCli = []
morada = []
tel = []
nif = []
compra = []
DivFin = []

prox_numcli = 1

while True:
    print("\n===== MENU =====")
    print("1 - Inserir")
    print("2 - Listar")
    print("3- Procurar")
    print("4 - Sair")
    opc = input("introduza uma opção: ")
    match opc:
        case "1":
            nome = input("Nome: ")
            while nome == "":
                print ("Não pode estar vazio")
                nome = input("Nome: ")
            mor = input("Morada: ")
            while mor == "":
                print ("Não pode estar vazio")
                mor = input("Morada: ")
            tele = input("Numero de Telemovel: ")
            while not tele.isdigit() or len(tele) != 9:
                print("O telemóvel deve ter exatamente 9 dígitos numéricos.")
                tele = input("Numero de Telemovel: ")
            ni = input("Nif: ")
            while not ni.isdigit() or len(ni) != 9:
                print("O NIF deve ter exatamente 9 dígitos numéricos.")
                ni = input("Nif: ")
            compr = float(input("Compra: "))
            while compr < 0:
                print ("Não pode ser negativo")
                compr = float(input("Compra: "))

            # calcular divida 
            if 100 <= compr <= 200:
                desconto = 0.05
            elif 200 < compr <= 500:
                desconto = 0.10
            elif compr > 500:
                desconto = 0.15
            else:
                desconto = 0.0 
            divin = compr * (1 - desconto)     

            # gravar nas listas
            NumCli.append(prox_numcli)
            NomCli.append(nome)
            morada.append(mor)
            tel.append(tele)
            nif.append(ni)
            compra.append(compr)
            DivFin.append(divin)    

            print(f"Cliente inserido com sucesso. NumCli = {prox_numcli}")
            prox_numcli += 1

        case "2":
            if len(NumCli) == 0:
                print("Nenhum cliente registado.")
            else:
                print("Lista de Clientes")      
                for i in range(len(NumCli)):
                    print(f"Número: {NumCli[i]} | Nome: {NomCli[i]} | Morada: {morada[i]} | Telefone: {tel[i]} | NIF: {nif[i]} | Compra: {compra[i]} | Dívida Final: {DivFin[i]}")
                    print("--------------------------------------------------------------")

        case "3":
            searchIndex=int(input("Introduza o Numero do cliente que procura: "))
            if searchIndex in NumCli:
                i = NumCli.index(searchIndex)
                print(f"Número: {NumCli[i]} | Nome: {NomCli[i]} | Morada: {morada[i]} | Telefone: {tel[i]} | NIF: {nif[i]} | Compra: {compra[i]} | Dívida Final: {DivFin[i]}")
            else:
                print("Cliente não encontrado")           

        case "4":
            print("Sair Do Programa")
            break

        case _:
            print("Opção Errada")