lista_pares = []
lista_impares = []
lista_numeros = []
while True:
    numero = input("Digite um número (ou pressione Enter para encerrar): ")
    if numero == "":
        break
    lista_numeros.append(int(numero))
print(f"{lista_numeros}")
for num in lista_numeros:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print(f"{lista_pares}")
print(f"{lista_impares}")