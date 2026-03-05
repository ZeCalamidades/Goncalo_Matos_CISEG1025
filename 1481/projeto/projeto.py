import re as regex


# regex.search()
# regex.match()
# regex.findall()
# regex.split()

#Texto="Eu gosto de Sushi, amanhã dia 25 é dia de jantarada"
email="bruh@gmail.com"
padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

resultado=regex.match(padrao,email)
#resultado= regex.search(r"\d+",Texto)

print(resultado) 
print(resultado.group())
print(resultado.start())
print(resultado.end())
print(resultado.span()) 
 

