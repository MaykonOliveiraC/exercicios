lista_numeros = []
numero5 = 5
while True:
    numero = input("Digite um número (ou pressione Enter para encerrar): ")
    if numero == "":
        break
    lista_numeros.append(int(numero))
lista_numeros.sort(reverse=True)
print("Lista de números:", lista_numeros)
numeros_digitados = len(lista_numeros)
print(f"Foram digitados {numeros_digitados} numeros.")
if numero5 not in lista_numeros:
    print(f"{numero5} não está na lista.")
else:
    print(f"{numero5} está na lista")
