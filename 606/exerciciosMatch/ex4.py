valor = input("Digite um valor: ")
def classificar_valor(v):
    try:
        int(v)
        return "inteiro"
    except ValueError:
        try:
            float(v)
            return "decimal"
        except ValueError:
            if v.startswith("[") and v.endswith("]"):
                return "lista"
            elif v.isdigit():
                return "string_numérica"
            elif v.isalpha() or " " in v:
                return "string_textual"
            else:
                return "desconhecido"
match tipo:
    case "inteiro":
        print("Número inteiro")
    case "decimal":
        print("Número decimal")
    case "string_numérica":
        print("String numérica")
    case "string_textual":
        print("String textual")
    case "lista":
        print("Lista")
    case _:
        print("Tipo desconhecido")