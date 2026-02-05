alunos = {}

while True:
    print("\n1 - Inserir aluno")
    print("2 - Listar alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")

        alunos[nome] = {
            "idade": idade,
            "curso": curso
        }

        print("Aluno inserido com sucesso!")

    elif opcao == "2":
        if not alunos:
            print("Não existem alunos.")
        else:
            for nome, dados in alunos.items():
                print("\nNome:", nome)
                print("Idade:", dados["idade"])
                print("Curso:", dados["curso"])

    elif opcao == "0":
        print("Adeus")
        break

    else:
        print("Opção inválida!")