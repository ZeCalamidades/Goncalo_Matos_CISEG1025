categoria = input("Introduz a categoria:")
preco = float(input("Escreva o preço:"))

produto = {"categoria": categoria, "preco": preco}

match produto:
    case{"categoria": "eletronico", "preco": preco} if preco > 1000:
        print("Produto de luxo")
    case{"categoria": "eletronico", "preco": preco} if preco <= 1000:
        print("Produto comum")
    case{"categoria": "alimento", "preco": preco}:
        print("Produto Alimentar") 
    case _:
        print("Categoria Desconhecida")          
