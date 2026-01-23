num1 = int(input("Insira um numero:"))
num2= 1

while num2 < num1:
    soma= num1+num2
    sub= num1-num2
    mult=num1*num2
    div=num1/num2
    print(f"{num1}+{num2}={soma}")
    print(f"{num1}-{num2}={sub}")
    print(f"{num1}*{num2}={mult}")
    print(f"{num1}/{num2}={div}") 
    num2 +=1
