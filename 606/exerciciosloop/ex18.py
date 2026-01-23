num = int(input("Insira um numero:"))
count=0

for tot in range(1, num+1):
    div=1
    soma=0
    
    while div < tot:
        if tot % div == 0:
            soma += div
        div += 1
            
    if soma == tot:
        print(f"{tot} é um numero perfeito")
        count +=1

print(f"Existem {count} numeros perfeitos entre 1 e {num}")            
