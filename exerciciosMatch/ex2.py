nota=int(input("Coloca a a tua nota:"))

match nota:
    case nota if nota<100 and nota>=90:
        print("Excelente")
    case nota if nota<90 and nota>=70:
        print("Bom")
    case nota if nota<79 and nota>=50:     
        print("Suficiente")
    case nota if nota<50:
        print("Insuficiente")
    case _:
        print("Erro")    