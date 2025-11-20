def check():
    # validar entrada entre 1 e 30000
    while True:
        try:
            insert = int(input("Coloque um valor entre 1 e 30000: "))
            if 1 <= insert <= 30000:
                break
            else:
                print("Valor fora do intervalo!")
        except:
            print("Digite um número válido!")

    contador = 0  # para pausar a cada 10

    for valor in range(1, insert + 1):

        # ----- verificar primo -----
        if valor <= 1:
            primo = False
        else:
            primo = True
            div = 2
            while div < valor:
                if valor % div == 0:
                    primo = False
                    break
                div += 1

        # ----- contar divisores -----
        total = 0
        div = 1
        while div <= valor:
            if valor % div == 0:
                total += 1
            div += 1

        # ----- verificar perfeito -----
        soma = 0
        div = 1
        while div < valor:
            if valor % div == 0:
                soma += div
            div += 1

        perfeito = (soma == valor)

        # ----- mostrar resultados -----
        print(f"Valor {valor} | Primo: {'Sim' if primo else 'Não'} | Divisores: {total} | Perfeito: {'Sim' if perfeito else 'Não'}")

        # pausa a cada 10 números
        contador += 1
        if contador == 10:
            continuar = input("Mostrar mais 10? (S/N): ").upper()
            if continuar != "S":
                print("A parar...")
                break
            contador = 0  # reset à contagem


def calculadora():
    while True:
        print("\nOpções: + | - | * | / | tabuada | sair")
        ope = input("Escolha a operação: ").lower()

        if ope in ["+", "-", "*", "/"]:
            # validar números
            try:
                num1 = float(input("Coloque o primeiro valor: "))
                num2 = float(input("Coloque o segundo valor: "))
            except:
                print("Número inválido.")
                continue

            if ope == "+":
                print("Resultado:", num1 + num2)
            elif ope == "-":
                print("Resultado:", num1 - num2)
            elif ope == "*":
                print("Resultado:", num1 * num2)
            elif ope == "/":
                if num2 == 0:
                    print("Erro: divisão por zero!")
                else:
                    print("Resultado:", num1 / num2)

        elif ope == "tabuada":
            # validar limite de 1 a 1000
            while True:
                try:
                    num = int(input("Insira um número de 1 a 1000: "))
                    if 1 <= num <= 1000:
                        break
                    else:
                        print("Valor fora do intervalo!")
                except:
                    print("Digite um número válido!")

            contador = 0
            for i in range(1, num + 1):
                print(f"{i} x {num} = {i * num}")
                contador += 1

                if contador == 20:
                    input("ENTER para continuar...")
                    contador = 0

        elif ope == "sair":
            return
        else:
            print("Opção inválida.")


def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Teste Final (Primos / Divisores / Perfeitos)")
        print("2 - Calculadora")
        print("0 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "0":
            print("Programa encerrado.")
            break
        elif opc == "1":
            check()
        elif opc == "2":
            calculadora()
        else:
            print("Opção inválida! Tente novamente.")


menu()
