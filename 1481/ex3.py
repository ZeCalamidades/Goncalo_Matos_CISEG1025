nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

def criterio(nome):
    partes = nome.split(" ")
    primeiro_nome = partes[0]
    apelido = partes[1]
    return (primeiro_nome, apelido)

nomes_ordenados = sorted(nomes, key=criterio)

print(nomes_ordenados)
