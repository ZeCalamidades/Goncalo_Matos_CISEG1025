metodo = input("Introduz o método: ")
conteudo = input("Introduz o conteudo: ")
requisicao = {"metodo": metodo, "conteudo":conteudo}

match requisicao:
    case{"metodo": "GET", "conteudo": _}:
        print("Requisição GET recebida")
    case{"metodo": "POST", "conteudo": c} if c!="":
        print("Requisição POST com dados válidos")
    case{"metodo": "POST", "conteudo": c} if c =="":
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")       