def compare_strings(a, b):
    for i in range(min(len(a), len(b))):
        if ord(a[i]) < ord(b[i]):
            return -1  
        elif ord(a[i]) > ord(b[i]):
            return 1   
    if len(a) < len(b):  
        return -1
    elif len(a) > len(b): 
        return 1
    return 0  
def sort_alphabetical(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_strings(words[j], words[j + 1]) > 0:
                words[j], words[j + 1] = words[j + 1], words[j]  
    return words
# Resultado
lista = ["banana", "uva", "abacaxi", "laranja"]
resultado = sort_alphabetical(lista)
print(resultado)