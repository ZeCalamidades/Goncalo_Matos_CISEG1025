nome = []
turma = []


while True:
    print("-----Cadastro de Alunos-----")
    print("1- Registar novo aluno")
    print("2- Procurar aluno por nome ou turma")
    print("3- Eliminar aluno por posição")
    print("4- Ordenar alunos por ordem alfabética")
    print("5- Listar turmas e alunos pertencentes")
    print("6- Sair do Programa")
    opc = input("Escolha a opção: ")
    match opc:
        case "1":
            if len(nome) < 100: 
                name = input("Insira o nome do aluno: ")
                while name.strip() == "":
                    print("O nome não pode estar vazio")
                    name = input("Insira o nome do aluno: ")
                tur = input("Insira a turma: ")
                while tur not in ["1ºA", "1ºB", "2ºA", "2ºB", "3ºA", "3ºB", "4ºA", "4ºB"]:
                    print("Turma não existe")
                    tur = input("Insira a turma: ")
            else:
                print("A base de dados está cheia")      
            existe = False    
            for i in range(len(nome)):
                if name == nome[i] and tur == turma[i]:
                    print("O aluno já está inserido nesta turma.")
                    existe = True
                    break       
            if existe != True:
                nome.append(name)
                turma.append(tur)  
                print(f"O aluno {name} foi inserido na turma {tur}.")  
        case "2":
            pesquisa = input("O que deseja pesquisar: ")
            for i in range(len(nome)):
                if pesquisa == nome[i] or pesquisa == turma[i]:
                    print(f"Posição: {[i]} | Nome do Aluno: {nome[i]} | Turma {turma[i]}")
                else:
                    print("Pesquisa não encontrada")    
            
        case "3":
            for i in range(len(nome)):
                print(f"Posição: {[i]} | Nome do Aluno: {nome[i]} | Turma {turma[i]}")
                print("-------------------------------------------------------------")
            


        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case _:
            pass