segundos = int(input("Insira o número de segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60

if horas == 1:
    h_texto = "1 hora"
else:
    h_texto = f"{horas} horas"

if minutos == 1:
    m_texto = "1 minuto"
else:
    m_texto = f"{minutos} minutos"

if segundos_restantes == 1:
    s_texto = "1 segundo"
else:
    s_texto = f"{segundos_restantes} segundos"

print(f"{h_texto}, {m_texto} e {s_texto}.")
