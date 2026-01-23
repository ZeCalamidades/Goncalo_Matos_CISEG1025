status = input("Escreve o status do servidor (ok ou erro): ")
try:
    tempo_resposta = int(input("Digite o tempo de resposta: "))
except ValueError:
    print("Tempo de resposta inválido! Digite um número inteiro.")
    exit()


server = {"status": status, "tempo_resposta": tempo_resposta}

match server:
    case {"status": "ok", "tempo_resposta": tempo} if tempo > 200:
        print("Servidor lento")
    case {"status": "ok", "tempo_resposta": _}:
        print("Servidor ativo")
    case {"status": "erro", "tempo_resposta": _}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")