frase = input("Digite uma frase:")

match frase:
    case "Ola" | "Olá" | "bom dia":
        print("Saudação")
    case _ if frase.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in frase or "adeus" in frase:
        print("Despedida")
    case _:
        print("Mensagem genérica")   
