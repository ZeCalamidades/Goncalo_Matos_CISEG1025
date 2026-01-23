titulo = []
autor = []
ano = []



while True:
    print("----- Catálogo de Livros -----")
    print("1- Adicionar novo livro")
    print("2- Procurar por título ou autor")
    print("3- Excluir livro")
    print("4- Ordenar livros")
    print("5- Listar livros")
    print("6- Sair do Programa")
    opc = input("Escolha a opção: ")
    match opc:
        case "1":    
            title = input("Introduza o titulo: ")
            writer = input("Introduza o autor: ")
            year = input("Introduza o ano: ")
            livro_existe = False
            for i in range(len(titulo)):
                if title == titulo[i] and writer == autor[i] and year == ano[i]:
                    livro_existe = True
                    break
            if livro_existe:
                print("Livro já existente")
                escolha = input("Pretende continuar? (s/n): ")  
                if escolha == "n":
                    print("Livro não inserido")
                else:
                    if len(titulo) >= 100:
                        print("Limite de livros atingido")
                    else:
                        titulo.append(title)
                        autor.append(writer)
                        ano.append(year)
                        print("Inserido com sucesso")
            else:
                if len(titulo) >= 100:
                        print("Limite de livros atingido")
                else:
                    titulo.append(title)
                    autor.append(writer)
                    ano.append(year)
                    print("Inserido com sucesso")

        case "2":
            procura = input("Introduza o titulo ou autor: ")
            for i in range(len(titulo)):
                if procura in titulo[i] or procura in autor[i]:
                    print(f"{i} | Titulo:{titulo[i]} | Autor:{autor[i]} | Ano de Publicação:{ano[i]}")
                else:
                    print("Nenhum livro encontrado")
        case "3":
            for i in range(len(titulo)):
                print(f"Indice:{i} | Titulo:{titulo[i]} | Autor:{autor[i]} | Ano de Publicação:{ano[i]}")
                print("---------------------------------------------------------------")
                apaga = int(input(("Qual o Indice do livro que deseja apagar: ")))
                if apaga in range(len(titulo)):
                    titulo.pop(apaga)
                    autor.pop(apaga)
                    ano.pop(apaga)
                    print("Apagado com sucesso")
                else:
                    print("Livro não encontrado")    
        case "4":
            print("1 - Ordenar Por Titulo")
            print("2 - Ordenar Por Autor")
            ordenar = input("Como quer Ordenar: ")
            if ordenar == "1":
                ordem = sorted(range(len(titulo)), key= lambda i: titulo[i].lower() )
            elif ordenar == "2":
                ordem = sorted(range(len(autor)), key= lambda i: autor[i].lower() )
            else:
                print("Opção não reconhecida")
                continue
            titulo = [titulo[i] for i in ordem]
            autor  = [autor[i] for i in ordem]
            ano    = [ano[i] for i in ordem]
            print("Ordenado com sucesso")
            print("Nova Listagem dos Livros:")
            for i in range(len(titulo)):
                print(f"Titulo:{titulo[i]},Autor:{autor[i]},Ano de Publicação:{ano[i]}")
                print("---------------------------------------------------------------")

        case "5":
            if len(titulo) < 1:
                print("Não tem livros")
            else:    
                print("Lista de Livros:")
                for i in range(len(titulo)):
                    print(f"Titulo:{titulo[i]},Autor:{autor[i]},Ano de Publicação:{ano[i]}")
                    print("---------------------------------------------------------------")
        case "6":
            print("Fica chefe")
            break
        case _:
            print("Opção não reconhecida")