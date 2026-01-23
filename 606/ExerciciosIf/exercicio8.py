notas = []
for i in range(10):
    nota = float(input(f"Insira a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / 10

acima_media = 0
for nota in notas:
    if nota >= media:
        acima_media += 1

print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_media}")
