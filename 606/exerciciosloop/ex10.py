soma = 0
div = 1
num = int(input("Insira um numero:"))

while div <= num:
    if num % div == 0:
        soma +=1
    div +=1
print(f"O numero tem {soma} divisores")    