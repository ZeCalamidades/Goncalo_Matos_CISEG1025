def calcular_chave_numerica(chave):
    if not chave:
        raise ValueError("A chave não pode ser vazia.")
    return sum(ord(c) for c in chave)


def criptografar(mensagem, chave):
    chave_numerica = calcular_chave_numerica(chave)
    codigos = []

    for c in mensagem:
        ascii_original = ord(c)
        ascii_criptografado = 32 + ((ascii_original - 32 + chave_numerica) % 95)
        codigos.append(ascii_criptografado)

    return codigos


def descriptografar(codigos, chave):
    chave_numerica = calcular_chave_numerica(chave)
    mensagem = ""

    for codigo in codigos:
        ascii_original = 32 + ((codigo - 32 - chave_numerica) % 95)
        mensagem += chr(ascii_original)

    return mensagem


def listar(codigos):
    print("Códigos criptografados:")
    for codigo in codigos:
        print(codigo, end=" ")
    print()

