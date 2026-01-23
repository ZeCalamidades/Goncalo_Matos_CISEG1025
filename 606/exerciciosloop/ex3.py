count = 1
total = 0

while count <= 10:
    nota = float(input(f"Digite a {count}ª nota:"))
    total += nota
    count += 1  
    
media = total / 10    
print(f"A média é igual a {media}")    
