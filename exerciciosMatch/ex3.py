tipo = input("Digite o tipo de pedido (compra ou venda): ")
valor = int(input("Digite o valor (€): "))


pedido = {"tipo": tipo, "valor": valor}


match pedido["tipo"]:
    case "compra":
        print(f"Compra de {pedido['valor']}€")
    case "venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido desconhecido")
