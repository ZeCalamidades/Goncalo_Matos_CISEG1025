count = 1

while count <=1000:
    if count % 5 == 0:
        if count % 3 != 0:
            print(count)
    else:
        count +=1    
        continue
    count +=1