dia=(input("Diga o dia da semana:"))


match dia:
    case "segunda"|"terça"|"quarta"|"quinta"|"sexta":
        print("Dia util")
    case "sabado"|"domingo":
        print("Fim de Semana")  
    case _:
        print("Dia inválido. Digite um dia da semana válido.")      