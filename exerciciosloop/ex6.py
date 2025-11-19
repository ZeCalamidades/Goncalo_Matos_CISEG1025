num = 2
count = 1

while count <= 10:
    div = 2
    primo=True

    while div < num:
        if num % div == 0:
            primo = False
            break
        div += 1
    
    if primo:
        print(num)
        count += 1

    num += 1