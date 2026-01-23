num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort()

print("Crescente:", numeros)
print("Decrescente:", list(reversed(numeros)))
