horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))
segundos = minutos * 60
segundos = horas * 3600

print(f"O tempo em segundos é = {segundos:.2f}.")

