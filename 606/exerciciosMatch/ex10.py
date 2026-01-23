jog1 = input("Introduz a jogada: ")
jog2 = input("Introduz a jogada: ")

jogo = {"jog1":jog1 , "jog2": jog2}

match jogo:
    case {"jog1":a , "jog2": b} if a=="pedra" and b=="tesoura" or a=="tesoura" and b=="papel" or a=="papel" and b=="pedra":
        print("Jogador 1 ganha")
    case {"jog1":a , "jog2": b} if b=="pedra" and a=="tesoura" or b=="tesoura" and a=="papel" or b=="papel" and a=="pedra":
        print("Jogador 2 ganha")
    case{"jog1":a , "jog2": b} if a == b:
        print("Empate")
    case _:
        print("Inválido")


