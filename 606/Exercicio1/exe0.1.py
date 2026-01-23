num1=int(input("Introduz o primeiro numero:"))
num2=int(input("Introduz o segundo numero:"))
num3=int(input("Introduz o terceiro numero:"))

if num1>num2 and num2>num3:
    print(f" O numero intermedio é {num2}")
elif num1>num3 and num3>num2:
    print(f" O numero intermedio é {num3}")
if num2>num1 and num1>num3:
    print(f" O numero intermedio é {num1}")    
elif num2>num3 and num3>num1:
    print(f" O numero intermedio é {num3}")    
if num3>num2 and num2>num1:
    print(f" O numero intermedio é {num2}")    
elif num3>num1 and num1>num2:
    print(f" O numero intermedio é {num1}")        