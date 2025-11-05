nota1 = float(input("Insira a 1ª nota: "))
nota2 = float(input("Insira a 2ª nota: "))
nota3 = float(input("Insira a 3ª nota: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"Média: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
