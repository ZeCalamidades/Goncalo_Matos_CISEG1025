operacao = input("Coloca a operação: ")
num1 = float(input("Coloca o primeiro numero: "))
num2= float(input("Coloca o segundo numero: "))

match operacao:
    case "soma":
        print(num1 + num2)
    case "subtrai":
        print(num1 - num2)
    case "multiplica":
        print(num1 * num2)    
    case "divide":
        print(num1 / num2)    
    case _:
        print("ERRO")    