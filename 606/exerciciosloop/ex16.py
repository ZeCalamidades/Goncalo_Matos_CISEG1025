count = 0
soma = 0

while count < 30:
    num = int(input("Insira um numero:"))


    if num % 2 != 0:
        print("Erro")
        continue
    if num < 1 or num > 50:
        print("Erro")
        continue
    soma += num
    count +=1
media = soma/30
print(f"A média é {media}")