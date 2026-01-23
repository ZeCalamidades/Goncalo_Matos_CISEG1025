num = int(input("Introduza um numero:"))

if num <= 1:
    print("Não é primo")
else:
    div = 2
    primo = True

    while div < num:
        if num % div == 0:
            primo = False
            break
        div += 1
    if primo : 
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")
