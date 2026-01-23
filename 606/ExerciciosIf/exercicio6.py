nome = input("Insira o nome do cliente: ")
valor = float(input("Insira o valor da compra (€): "))

if valor <= 200:
    desconto = valor * 0.10
elif valor <= 500:
    desconto = valor * 0.15
else:
    desconto = valor * 0.20

total = valor - desconto

print(f"\nNome: {nome}")
print(f"Compra: {valor:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total:.2f}€")
