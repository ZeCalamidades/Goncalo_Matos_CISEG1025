nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

it=0
tamanho=0

for i in range(len(nomes)-1):
    it=0
    tamanho=len(nomes[i])
    while it< tamanho:
        print("pos1=",nomes[i],"pos2=",nomes[i+1])
        print("Letra pos1",nomes[i][it],"Letra pos2",nomes[i+1][it])
        if len(nomes[i]) > len(nomes[i+1]):
            tamanho=len(nomes[i+1])
        if ord(nomes[i][it]) > ord(nomes[i+1][it]):
            nomes[i],nomes[i+1]=nomes[i+1],nomes[i]
        it+=1
print(nomes)