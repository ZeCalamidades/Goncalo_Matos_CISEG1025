cod = 0

while cod <= 255:
    for i in range(20):
        if cod >255:
            break
        try:
            char = chr(cod)
        except:
            char = "?"    
        print(f"Código: {cod:3}  |  Carácter: {repr(char)}")
        cod +=1
    if cod <= 255:
        cont = input("\nContinuar? (S/N): ")
        if cont.lower() == "n":
            break
