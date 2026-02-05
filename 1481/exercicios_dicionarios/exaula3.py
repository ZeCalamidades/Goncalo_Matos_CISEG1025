listadicionario=[{ "nome":"Joao", "Tele": [965555,989999] },{ "nome":"Pedro", "Tele":[966666,95000]}]
 

for dicionario in listadicionario:
    print("Nome:", dicionario["nome"])
    for tel in dicionario["Tele"]:
        print("  Tel:", tel)
    print("-----")
