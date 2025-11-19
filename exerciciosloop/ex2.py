count = 1

while count <= 10:
    num = int(input(f"Digite o {count}º numero:"))

    if num % 2 == 0:
        print(f"{num} é par")
    
    else:
        print(f"{num} é inpar")
    count += 1       
     