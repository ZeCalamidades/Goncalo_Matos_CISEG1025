nome = input("Introduza o nome completo: ")

if ord(nome[0]) < ord('A') or ord(nome[0]) > ord('Z'):
    print("Nome inválido: contém caracteres não permitidos.")
    exit()

for i in range(len(nome)):

    codigo = ord(nome[i])

    if not (
        (ord('A') <= codigo <= ord('Z')) or
        (ord('a') <= codigo <= ord('z')) or
        codigo == ord(' ')
    ):
        print("Nome inválido: contém caracteres não permitidos.")
        exit()

    if nome[i] == ' ' and i + 1 < len(nome):
        prox = ord(nome[i + 1])
        if prox < ord('A') or prox > ord('Z'):
            print("Nome inválido: contém caracteres não permitidos.")
            exit()

print("Nome válido!")
nome = input("Introduza o nome completo: ")

if ord(nome[0]) < ord('A') or ord(nome[0]) > ord('Z'):
    print("Nome inválido: contém caracteres não permitidos.")
    exit()

for i in range(len(nome)):

    codigo = ord(nome[i])

    if not (
        (ord('A') <= codigo <= ord('Z')) or
        (ord('a') <= codigo <= ord('z')) or
        codigo == ord(' ')
    ):
        print("Nome inválido: contém caracteres não permitidos.")
        exit()

    if nome[i] == ' ' and i + 1 < len(nome):
        prox = ord(nome[i + 1])
        if prox < ord('A') or prox > ord('Z'):
            print("Nome inválido: contém caracteres não permitidos.")
            exit()

print("Nome válido!")
