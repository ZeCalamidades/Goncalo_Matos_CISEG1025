saldo = float(input("Insira o saldo disponível: "))
cheque = float(input("Insira o valor do cheque: "))

if cheque > saldo:
    print("O cheque não pode ser descontado. Saldo insuficiente.")
else:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo:.2f}€")
